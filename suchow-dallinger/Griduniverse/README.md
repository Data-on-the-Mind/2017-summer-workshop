# Griduniverse


Reinforcement learning is an area of machine learning that considers the problem faced by a decision-maker in a setting partly under control of the environment. To illustrate the complexities of learning in even simple scenarios, researchers often turn to so-called “Gridworlds”, toy problems that nonetheless capture the rich difficulties that arise when learning in an uncertain world. By adjusting the state space (i.e., the grid), the set of actions available to the decision maker, the reward function, and the mapping between actions and states, a richly structured array of reinforcement learning problems can be generated — a Griduniverse, one might say. To design a successful reinforcement learning AI system, then, is to develop an algorithm that learns well across many such Gridworlds. Indeed, state-of-the-art reinforcement learning algorithms such as deep Q-networks, for example, have achieved professional-level performance across tens of video games from raw pixel input.  

Fig. 1. A small Gridworld, reprinted from Sutton & Barto (1998). At each time step, the agent selects a move (up, down, left, right) and receives the reward specified in the grid.

Here, we create a Griduniverse for the study of human social behavior — a parameterized space of games expansive enough to capture a diversity of relevant dynamics, yet simple enough to permit rigorous analysis. We begin by documenting parameters of the Griduniverse. We then describe a broad set of existing experimental paradigms and economic games that exists as worlds in this universe. To build a successful model of collective identity formation is to create one that can explain many such worlds.

## Elements of the Griduniverse

### Grid

A Gridworld contains a grid (GRID_HEIGHT, GRID_WIDTH). For example, Fig. 2 shows two players on a 20 × 20 grid.
 
Fig. 2. Two players on a 20 × 20 grid.

### Players

A set of players inhabit the Gridworld (N). Each player has a position on the grid (INITIAL_POSITION). Players may be controlled by human participants, bots, bionics, or some combination.

Players may have control over their position on the grid (IS_PLAYER_MOTION). If players can control their position, it may be in one of two ways — through actions that change the direction of always present motion, or that change the position of an otherwise motionless player (IS_MOTION_PERPETUAL). Each player has a fixed maximum speed of motion (SPEED), which may vary across players. Players may be able to move and change direction throughout the game, or there may be actions that prevent further motion (FREEZING_ACTIONS).

Players take on one of some number of distinguishable identities (NUM_IDENTITIES). Players may select their identity of it may be assigned to them (IS_IDENTITY_SELECTED). Players may be allowed to move freely between identities (IS_IDENTITY_FLUID). Players may be able to see the identity of others. Ability to see the identity of others may depend on their position on the grid, the identity of the player or the other player, or the network structure. Identities may be transmissible based on spatial proximity or network structure.


Fig. 3. Sample colors that could serve as distinguishable identities.

### Objects

The world may contain non-player objects that are immovable (e.g., walls) or movable (e.g., blocks).

### Chatroom

Players may be given a free-form chatroom that allows them to communicate with others (IS_CHATROOM). If there is a chatroom, players may be able to communicate only with those who share an identity (IS_CHAT_WITH_OTHERS), are neighbors in their social network, or are within some distance from the player (CHATROOM_MIN_DISTANCE).

### Social network

Players are situated in a social network that may determine who they can see or chat with. Players may be able to rewire the network by forging or breaking links.

### Score

Players have a score that determines their payout in the game. A players score rises and falls depending on their actions and those of others. Players may receive points based on their location, proximity to others in a network, random chance, and their interactions with others.

### Actions

Players may be able to interact with other players. For example, players may be able to transfer some or all of their score to others (IS_REWARD_OTHERS, MAX_REWARD_TO_OTHERS, IS_REWARD_TO_OTHERS_ALL_OR_NONE), and this transference may be limited by position, network structure, or identity.

### Gameplay

The game may have multiple rounds (NUM_ROUNDS). Each round may last until a particular outcome or for a given amount of time (STOPPING_RULE).

### In-game questionnaire

At various points, the game may pause and players will be asked to respond to the Dynamic Identity Fusion Index survey instrument as it pertains to a particular identity. Players may also be asked to complete a longer survey instrument. These survey instruments may also be administered at the close of the game.

### Metagame questionnaire

Players will be asked various questions that exist outside the Griduniverse. At the beginning of the study, they will be asked to consent. At the end of the study, they will be asked to answer questions about the difficulty of the game and their engagement with it.

## Case study of a Gridworld, 1: the zombie game

Over the past several years, a vibrant ecosystem of accessible web technologies (e.g. WebSockets) has led to the proliferation of interactive multiplayer online games. One such class of these games are the so-called “io” games (http://iogames.space/), named for the top-level domain on which they are often hosted (.io). In a typical io game, a moderate number of people (10-100) compete for resources in a fast-paced action game that lasts several minutes. The game is then repeated. Our team recently found an io game with great relevance to the problem of collective identity formation: braains.io.

Braains is a game in the popular zombie genre, inspired by horror films, B movies, and literature. In the game, a set of 3-100 players are placed in a random position in a multi-roomed house with a yard. Players have a birds-eye view of a house and can control their position using their keyboard. Before the game begins, all players are assigned the identity of “human” and are free to roam about the house and move objects within it. A timer at the top of the screen counts down until the game begins. When the game begins, one player is selected at random and is reassigned a new identity: “zombie”, taking on a new appearance. The player’s identity determines the payoff structure of the game. Zombies are rewarded for touching humans, who then become zombies. Humans are rewarded for each second that they are not a zombie.

Braains is an interesting case study in human social behavior and collective identity because of the rich array of behavior exhibited in the game. For example, a social dilemma often arises during the initial phase of the game. Players can collaborate to barricade rooms in such a way that they are inpenetrable by zombies (Fig. 4). Some rooms, however, can only be successfully barricaded by someone outside the room. That person pays the cost of helping but, by nature of the barricade, is prevented from receiving its benefits. This is a Volunteer’s Dilemma, as described by Schelling (1971). Later in the game, players begin to become infected by zombies. At the moment of infection, a player’s outward identity changes instantaneously. They are immediately stigmatized by their group, who runs from them. How do perceptions of identity change at this moment? When does a player come to feel a sense of belonging to the zombies? There are many questions that can be asked.

A minimal version of Braains is one world in the Griduniverse. 


Fig. 4. Screenshot of the Braains game. A group of humans act collectively to prevent intrusion from zombies, who similarly take collective action, but with opposite intentions.

Case study of a Gridworld, 1: the minimal group paradigm

The minimal group paradigm is an experimental paradigm from social psychology that considers the minimal conditions needed to induce in-group favoritism. The paradigm begins by assigning one of two identities to a set of players. Identities may be assigned randomly (e.g., red or blue as determined by a coin flip) or based on some dimension along which people vary (e.g., odd or even birth month). Players are then given the opportunity to divide a resource among pairs of other players. The choices are manipulated to tease apart various factors that may affect the resource allocation.

## GridUniverse configuration parameters

### max_participants

Number of players. Default is 3.


### num_rounds

Number of rounds. Default is 1.


### time_per_round

Time per round, in seconds. Defaults to 300.


### instruct

Whether to show instructions to the players or not. True by default.


### columns

Number of columns for the grid. Default is 25.


### rows

Number of rows for the grid. Default is 25.


### block_size

Size of each side of a block in the grid, in pixels. Defaults to 10.


### padding

Space between blocks, in pixels. Default is 1.


### visibility

The standard deviation (in blocks) of a gaussian visibility window centered on the
player. Default is 1000, so all grid is visible.


### background_animation

Play a background animation in the area visible to the player. Default is True.


### player_overlap

Whether two players can be on the same block at the same time. False by default.


### motion_speed_limit

This is the maximum speed of a player in units of blocks per second. Goes from 1
to 1000. Default is 16.


### motion_auto

Whether movement in the direction of previous player motion is automatic. This makes
the game similar to the snake game mentioned in the next section. Default is False.


### motion_cost

Cost in points for each movement. Default is 0.


### motion_tremble_rate

Rate of random direction change for player movement. From 0 to 1. A value of 0
means movement is always in the direction the player specified; a value of 1
means all movement is random.


### show_chatroom

Whether the chatroom appears in the UI. Defaults to True.


### show_grid

Show the grid in the UI. Defaults to True.


### others_visible

Whether other players are visible on the grid. Deafult is True.


### num_colors

Number of possible colors for a player. Defaults to 3.


### mutable_colors

Setting this to True allows players to change colors using the keyboard. False
by default.


### costly_colors

Controls whether changing color has a cost in points for each color. The cost
is a power of 2, starting as 2. Which color gets which cost is randomly
decided at the start of the game. Defaults to False.


### pseudonyms

Use generated pseudonyms instead of player numbers for chat messages. Defaults
to True.


### pseudonyms_locale

Locale for the generated pseudonyms. Defaults to en_US.


### pseudonyms_gender

Gender for the generated pseudonyms. Defaults to None.


### contagion

Distance from each player where a neighboring player can be "infected" and thus
become the color of the plurality of its neighbors. Default is 0, so no
contagion can occur.


### contagion_hierarchy

If True, assigns a random hierarchy to player colors, so that higher colors in
the hierarchy can spread to lower colors, but not vice versa. Default is False.


### walls_visible

Whether the maze walls, if any, are visible. Defaults to True.


### walls_density

Defines if the grid will have a maze and how many walls it will have. A density
of 0 means no walls, while 1 means the most possible walls. Default is 0.


### walls_contiguity

Whether the maze walls are contiguous or have random holes. The default, 1,
means contiguous.


### initial_score

Initial score for each player. Default is 0.


### dollars_per_point

How much will be gained by each player in US dollars when the game ends.
Default is $0.02.


### tax

Amount of points to tax each player for each second on the grid. Default is
0.01.


### relative_deprivation

When food is consumed, multiply food reward by this factor to get total reward.
Defaults to 1.


### frequency_dependence

The value here is used to calculate a payoff to add to the player's score
according to the frequency of their color. Higher values mean higher payoff. The
default is 0.


### frequency_dependent_payoff_rate

How big is the frequency dependent payoff. The payoff is multiplied by this
value. Default is 0.


### donation

Amount of donation, in points, that a player can make to another by clicking on
its color in the grid. Default is 0.


### num_food

Number of food blocks at game start. Default is 8.


### respawn_food

Whether to spawn food again after it is consumed. Defaults to True.


### food_visible

If True, food is visible on the grid, which is the default.


### food_reward

Value in points for each block of food. Default is 1.


### food_pg_multiplier

Amount to multiply for food reward to distribute among all players each time
food is cosumed. Default is 1.


### food_growth_rate

Rate at which food grows every second during the game. Default is 1.


### food_maturation_speed

Speed of increase in maturity for spawned food blocks. Default is 1.


### food_maturation_threshold

Maturity value required for food to be ready to consume. Defaults to 0.


### food_planting

If True, players can plant food using the space bar. False by default.


### food_planting_cost

How many points it costs for a player to plant food. Default is 1.


### seasonal_growth_rate

The rate of food store growth or shrinkage each second. In odd rounds the
food store grows, and it shrinks in even rounds. Default is 1.


### difi_question

Whether to asminister the Dynamic Identity Fusion Index (DIFI) at the
end of the game. Default is False.


### difi_group_label

The label to use for the group when asking the DIFI question at the end.


### difi_group_image

URI to the group image to use when asking the DIFI question at the end. Default
is "/static/images/group.jpg".


### leach_survey

If true, the Leach survey is applied as part of the ending questionnaire.
Default is False.

## Exploring the Griduniverse

A vast number of games, social dilemmas, and experimental paradigms for studying human social behavior can be expressed as worlds in the Griduniverse.

### Chicken

The game of chicken is one of brinkmanship. A pair of squares, one blue, one yellow, each begin on the same row of a 2 × 20 grid, moving inward toward each other. If they collide, both lose 10 points. If they pull to the side, they each gain nothing. If one pulls to the side and the other continues on course, the one who pulls to the side loses 5 and the one who continues gains 5.

Fig. 5. Screenshot of chicken.

### Schelling’s model of spatial segregation.

### Spatial Voronoi game.

### Matching penniesA 

A pair of squares, one blue, one yellow, each begin on different rows of a 2 x 20 grid, moving inward toward each other. If they collide, the blue square wins. If they pass by each other, the yellow square wins.

Fig. 6. Screenshot of chicken.

### Coordination game

A pair of squares, one blue, one yellow, each begin on different rows of a 2 x 20 grid, moving inward toward each other. Each wins if they collide and loses if they do not. Critically, they must choose whether to move before seeing the other’s decision.

### Battle of the sexes

### Negotiation game

### Blotto game

(Time-based resource.)

### Deadlock.

### Prisoner’s dilemma

### Minority game

An odd number of players each choose one of two colors. Players in the minority win. The game is iterated.

### Snake

A single player hunts for food in an environment, growing in length by one each time food is found. The player loses when the snake touches a side wall or itself.

### Dueling snakes

A pair of players hunt for food in an environment, growing in length by one each time food is found. A player loses when their snake touches a side wall, itself, or the other snake.

### Collective snake

### Schelling focal points

### Asch conformity experiments

### Poetic generator

### Maze 

A single player navigates a maze, searching for an exit.

### Reinforcement learning Gridworld

The Gridworlds that have been studied in reinforcement learning are special cases of the Griduniverse.

### Reduced Turing test

The participant plays a pair of identical Gridworld games, except that in one the participant plays with a bot and in the other, the participant plays with a human. At the end of the game, the participant is asked to identify the bot.
	
### Hedonic games

In a hedonic game, each of N players is assigned a unique identity and a partial order over subsets of players that include the ego that determines payoffs. these payoffs may conflict across players. Players are given a chance to form coalitions. Payoff is determined by the coalitions that are formed.

### Tag

In the game of tag, one player is designated “it”. That player’s goal is to touch another player, which transfers the identity of “it” to them. The game continues indefinitely or for some set amount of time.

### Irreversible tag

In the game of irreversible tag, one player is designated “it”. That player’s goal is to touch another player, who then joins the set of people designated as “it”. The game ends when everyone has the identity “it”. (This game is closely related to the zombie games.)

### Blob tag

In the game of blob tag, one player is designated “it”. That player’s goal is to touch another player, who then joins the set of people designated as “it”. Critically, all players with the identity “it” must take collective action in order to move.

