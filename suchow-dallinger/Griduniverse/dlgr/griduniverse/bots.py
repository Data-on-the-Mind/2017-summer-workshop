"""Griduniverse bots."""
import itertools
import json
import operator
import random
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from dallinger.bots import BotBase
from dallinger.config import get_config

config = get_config()


class BaseGridUniverseBot(BotBase):

    def wait_for_grid(self):
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "grid"))
        )

    def get_js_variable(self, variable_name):
        try:
            script = 'return window.{};'.format(variable_name)
            result = self.driver.execute_script(script)
            if result is None:
                # In some cases (older remote Firefox)
                # we need to use window.wrappedJSObject
                script = 'return window.wrappedJSObject.{};'.format(variable_name)
                result = self.driver.execute_script(script)
        except WebDriverException:
            result = None

        if result is not None:
            return json.loads(result)

    def observe_state(self):
        return self.get_js_variable("state")

    def get_player_id(self):
        return str(self.get_js_variable("ego"))

    @property
    def food_positions(self):
        try:
            return [tuple(item['position']) for item in self.state['food']
                    if item['maturity'] > 0.5]
        except (AttributeError, TypeError):
            return []

    @property
    def player_positions(self):
        return {
            player['id']: player['position'] for player in self.state['players']
        }

    @property
    def my_position(self):
        if self.player_positions:
            return self.player_positions[self.player_id]
        else:
            return None

    def send_next_key(self, grid):
        # This is a roundabout way of sending the key
        # to the grid element; it's needed to avoid a
        # "cannot focus element" error with chromedriver
        if self.driver.desired_capabilities['browserName'] == 'chrome':
            action = ActionChains(self.driver).move_to_element(grid)
            action.click().send_keys(self.get_next_key()).perform()
        else:
            grid.send_keys(self.get_next_key())


class RandomBot(BaseGridUniverseBot):
    """A bot that plays griduniverse randomly"""

    VALID_KEYS = [
        Keys.UP,
        Keys.DOWN,
        Keys.RIGHT,
        Keys.LEFT,
        Keys.SPACE,
        'r',
        'b',
        'y'
    ]

    KEY_INTERVAL = 0.1

    def get_next_key(self):
        return random.choice(self.VALID_KEYS)

    def get_wait_time(self):
        return random.expovariate(1.0 / self.KEY_INTERVAL)

    def participate(self):
        """Participate by randomly hitting valid keys"""
        grid = self.wait_for_grid()
        try:
            while True:
                time.sleep(self.get_wait_time())
                self.send_next_key(grid)
        except StaleElementReferenceException:
            pass
        return True


class AdvantageSeekingBot(BaseGridUniverseBot):
    """A bot that seeks an advantage.

    The bot moves towards the food it has the biggest advantage over the other
    players at getting.
    """

    KEY_INTERVAL = 0.1

    def get_logical_targets(self):
        """Find a logical place to move.

        When run on a page view that has data extracted from the grid state
        find the best targets for each of the players, where the best target
        is the closest item of food, excluding all food items that are the best
        target for another player. When the same item of food is the closest
        target for multiple players the closest player would get there first,
        so it is excluded as the best target for other players.

        For example:
        Player 1 is 3 spaces from food item 1 and 5 from food item 2.
        Player 2 is 4 spaces from food item 1 and 6 from food item 2.

        The logical targets are:
        Player 1: food item 1
        Player 2: food item 2
        """
        best_choices = {}
        # Create a mapping of (player_id, food_id) tuple to the distance between
        # the relevant player and food item
        for player, food_info in self.distances().items():
            for food_id, distance in food_info.items():
                best_choices[player, food_id] = distance
        # Sort that list based on the distance, so the closest players/food
        # pairs are first, then discard the distance
        get_key = operator.itemgetter(0)
        get_food_distance = operator.itemgetter(1)
        best_choices = sorted(best_choices.items(), key=get_food_distance)
        best_choices = map(get_key, best_choices)
        # We need to find the optimum solution, so we iterate through the
        # sorted list, discarding pairings that are inferior to previous
        # options. We keep track of player and food ids, once either has been
        # used we know that player or food item has a better choice.
        seen_players = set()
        seen_food = set()
        choices = {}
        for (player_id, food_id) in best_choices:
            if player_id in seen_players:
                continue
            if food_id in seen_food:
                continue
            seen_players.add(player_id)
            seen_food.add(food_id)
            choices[player_id] = food_id
        return choices

    def get_player_spread(self, positions=None):
        """Mean distance between players.

        When run after populating state data, this returns the mean
        distance between all players on the board, to be used as a heuristic
        for 'spreading out' if there are no logical targets.
        """
        # Allow passing positions in, to calculate the spread of a hypothetical
        # future state, rather than the current state
        if positions is None:
            positions = self.player_positions
        positions = positions.values()
        # Find the distances between all pairs of players
        pairs = itertools.combinations(positions, 2)
        distances = itertools.starmap(self.manhattan_distance, pairs)
        # Calculate and return the mean. distances is an iterator, so we
        # convert it to a tuple so we can more easily do sums on its data
        distances = tuple(distances)
        if distances:
            return float(sum(distances)) / len(distances)
        else:
            # There is only one player, so there are no distances between
            # players.
            return 0

    def get_expected_position(self, key):
        """Predict future state given an action.

        Given the current state of players, if we were to push the key
        specified as a parameter, what would we expect the state to become,
        ignoring modeling of other players' behavior
        """
        positions = self.player_positions
        my_position = positions[self.player_id]
        pad = 5
        rows = self.state['rows']
        if key == Keys.UP and my_position[0] > pad:
            my_position = (my_position[0] - 1, my_position[1])
        if key == Keys.DOWN and my_position[0] < (rows - pad):
            my_position = (my_position[0] + 1, my_position[1])
        if key == Keys.LEFT and my_position[1] > pad:
            my_position = (my_position[0], my_position[1] - 1)
        if key == Keys.RIGHT and my_position[1] < (rows - pad):
            my_position = (my_position[0], my_position[1] + 1)
        positions[self.player_id] = my_position
        return positions

    def get_next_key(self):
        valid_keys = []
        my_position = self.my_position
        try:
            # If there is a most logical target, we move towards it
            target_id = self.get_logical_targets()[self.player_id]
            food_position = self.food_positions[target_id]
        except KeyError:
            # Otherwise, move in a direction that increases average spread.
            current_spread = self.get_player_spread()
            for key in (Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT):
                expected = self.get_expected_position(key)
                if self.get_player_spread(expected) > current_spread:
                    valid_keys.append(key)
        else:
            if food_position[0] < my_position[0]:
                valid_keys.append(Keys.UP)
            elif food_position[0] > my_position[0]:
                valid_keys.append(Keys.DOWN)
            if food_position[1] < my_position[1]:
                valid_keys.append(Keys.LEFT)
            elif food_position[1] > my_position[1]:
                valid_keys.append(Keys.RIGHT)
        if not valid_keys:
            # If there are no food items available and no movement would
            # cause the average spread of players to increase, fall back to
            # the behavior of the RandomBot
            valid_keys = RandomBot.VALID_KEYS
        return random.choice(valid_keys)

    def get_wait_time(self):
        return random.expovariate(1.0 / self.KEY_INTERVAL)

    @staticmethod
    def manhattan_distance(coord1, coord2):
        x = coord1[0] - coord2[0]
        y = coord1[1] - coord2[1]
        return abs(x) + abs(y)

    def distances(self):
        """Compute distances to food.

        Returns a dictionary keyed on player_id, with the value being another
        dictionary which maps the index of a food item in the positions list
        to the distance between that player and that food item.
        """
        distances = {}
        for player_id, position in self.player_positions.items():
            player_distances = {}
            for j, food in enumerate(self.food_positions):
                player_distances[j] = self.manhattan_distance(position, food)
            distances[player_id] = player_distances
        return distances

    def participate(self):
        """Participate in the experiment.

        Wait a random amount of time, then send a key according to
        the algorithm above.
        """
        grid = self.wait_for_grid()

        # Wait for state to be available
        self.state = None
        self.player_id = None
        while (self.state is None) or (self.player_id is None):
            time.sleep(0.500)
            self.state = self.observe_state()
            self.player_id = self.get_player_id()

        while True:
            time.sleep(self.get_wait_time())
            try:
                observed_state = self.observe_state()
                if observed_state:
                    self.state = observed_state
                    self.send_next_key(grid)
            except (StaleElementReferenceException, AttributeError):
                return True

    def complete_questionnaire(self):
        """Complete the standard debriefing form."""
        pass


def Bot(*args, **kwargs):
    """Pick a bot implementation based on a configuration parameter.

    This can be set in config.txt in this directory or by environment variable.
    """

    bot_implementation = config.get('bot_policy', u'RandomBot')
    bot_class = globals().get(bot_implementation, None)
    if bot_class and issubclass(bot_class, BotBase):
        return bot_class(*args, **kwargs)
    else:
        raise NotImplementedError
