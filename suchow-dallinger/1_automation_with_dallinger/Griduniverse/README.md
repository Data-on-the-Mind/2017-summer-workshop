# Griduniverse

## max_participants

Number of players. Default is 3.


## num_rounds

Number of rounds. Default is 1.


## time_per_round

Time per round, in seconds. Defaults to 300.


## instruct

Whether to show instructions to the players or not. True by default.


## columns

Number of columns for the grid. Default is 25.


## rows

Number of rows for the grid. Default is 25.


## block_size

Size of each side of a block in the grid, in pixels. Defaults to 10.


## padding

Space between blocks, in pixels. Default is 1.


## visibility

The standard deviation (in blocks) of a gaussian visibility window centered on the
player. Default is 1000, so all grid is visible.


## background_animation

Play a background animation in the area visible to the player. Default is True.


## player_overlap

Whether two players can be on the same block at the same time. False by default.


## motion_speed_limit

This is the maximum speed of a player in units of blocks per second. Goes from 1
to 1000. Default is 16.


## motion_auto

Whether movement in the direction of previous player motion is automatic. This makes
the game similar to the snake game mentioned in the next section. Default is False.


## motion_cost

Cost in points for each movement. Default is 0.


## motion_tremble_rate

Rate of random direction change for player movement. From 0 to 1. A value of 0
means movement is always in the direction the player specified; a value of 1
means all movement is random.


## show_chatroom

Whether the chatroom appears in the UI. Defaults to True.


## show_grid

Show the grid in the UI. Defaults to True.


## others_visible

Whether other players are visible on the grid. Deafult is True.


## num_colors

Number of possible colors for a player. Defaults to 3.


## mutable_colors

Setting this to True allows players to change colors using the keyboard. False
by default.


## costly_colors

Controls whether changing color has a cost in points for each color. The cost
is a power of 2, starting as 2. Which color gets which cost is randomly
decided at the start of the game. Defaults to False.


## pseudonyms

Use generated pseudonyms instead of player numbers for chat messages. Defaults
to True.


## pseudonyms_locale

Locale for the generated pseudonyms. Defaults to en_US.


## pseudonyms_gender

Gender for the generated pseudonyms. Defaults to None.


## contagion

Distance from each player where a neighboring player can be "infected" and thus
become the color of the plurality of its neighbors. Default is 0, so no
contagion can occur.


## contagion_hierarchy

If True, assigns a random hierarchy to player colors, so that higher colors in
the hierarchy can spread to lower colors, but not vice versa. Default is False.


## walls_visible

Whether the maze walls, if any, are visible. Defaults to True.


## walls_density

Defines if the grid will have a maze and how many walls it will have. A density
of 0 means no walls, while 1 means the most possible walls. Default is 0.


## walls_contiguity

Whether the maze walls are contiguous or have random holes. The default, 1,
means contiguous.


## initial_score

Initial score for each player. Default is 0.


## dollars_per_point

How much will be gained by each player in US dollars when the game ends.
Default is $0.02.


## tax

Amount of points to tax each player for each second on the grid. Default is
0.01.


## relative_deprivation

When food is consumed, multiply food reward by this factor to get total reward.
Defaults to 1.


## frequency_dependence

The value here is used to calculate a payoff to add to the player's score
according to the frequency of their color. Higher values mean higher payoff. The
default is 0.


## frequency_dependent_payoff_rate

How big is the frequency dependent payoff. The payoff is multiplied by this
value. Default is 0.


## donation

Amount of donation, in points, that a player can make to another by clicking on
its color in the grid. Default is 0.


## num_food

Number of food blocks at game start. Default is 8.


## respawn_food

Whether to spawn food again after it is consumed. Defaults to True.


## food_visible

If True, food is visible on the grid, which is the default.


## food_reward

Value in points for each block of food. Default is 1.


## food_pg_multiplier

Amount to multiply for food reward to distribute among all players each time
food is cosumed. Default is 1.


## food_growth_rate

Rate at which food grows every second during the game. Default is 1.


## food_maturation_speed

Speed of increase in maturity for spawned food blocks. Default is 1.


## food_maturation_threshold

Maturity value required for food to be ready to consume. Defaults to 0.


## food_planting

If True, players can plant food using the space bar. False by default.


## food_planting_cost

How many points it costs for a player to plant food. Default is 1.


## seasonal_growth_rate

The rate of food store growth or shrinkage each second. In odd rounds the
food store grows, and it shrinks in even rounds. Default is 1.


## difi_question

Whether to asminister the Dynamic Identity Fusion Index (DIFI) at the
end of the game. Default is False.


## difi_group_label

The label to use for the group when asking the DIFI question at the end.


## difi_group_image

URI to the group image to use when asking the DIFI question at the end. Default
is "/static/images/group.jpg".


## leach_survey

If true, the Leach survey is applied as part of the ending questionnaire.
Default is False.
