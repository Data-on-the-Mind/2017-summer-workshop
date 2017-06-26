Griduniverse
============

Reinforcement learning is an area of machine learning that considers the
problem faced by a decision-maker in a setting partly under control of
the environment. To illustrate the complexities of learning in even
simple scenarios, researchers often turn to so-called “Gridworlds”, toy
problems that nonetheless capture the rich difficulties that arise when
learning in an uncertain world. By adjusting the state space (i.e., the
grid), the set of actions available to the decision maker, the reward
function, and the mapping between actions and states, a richly
structured array of reinforcement learning problems can be generated — a
Griduniverse, one might say. To design a successful reinforcement
learning AI system, then, is to develop an algorithm that learns well
across many such Gridworlds. Indeed, state-of-the-art reinforcement
learning algorithms such as deep Q-networks, for example, have achieved
professional-level performance across tens of video games from raw pixel
input.

Fig. 1. A small Gridworld, reprinted from Sutton & Barto (1998). At each
time step, the agent selects a move (up, down, left, right) and receives
the reward specified in the grid.

Here, we create a Griduniverse for the study of human social behavior —
a parameterized space of games expansive enough to capture a diversity
of relevant dynamics, yet simple enough to permit rigorous analysis. We
begin by documenting parameters of the Griduniverse. We then describe a
broad set of existing experimental paradigms and economic games that
exists as worlds in this universe. To build a successful model of
collective identity formation is to create one that can explain many
such worlds.

Elements of the Griduniverse
----------------------------

Grid
~~~~

A Gridworld contains a grid (GRID\_HEIGHT, GRID\_WIDTH). For example,
Fig. 2 shows two players on a 20 × 20 grid.

Fig. 2. Two players on a 20 × 20 grid.

Players
~~~~~~~

A set of players inhabit the Gridworld (N). Each player has a position
on the grid (INITIAL\_POSITION). Players may be controlled by human
participants, bots, bionics, or some combination.

Players may have control over their position on the grid
(IS\_PLAYER\_MOTION). If players can control their position, it may be
in one of two ways — through actions that change the direction of always
present motion, or that change the position of an otherwise motionless
player (IS\_MOTION\_PERPETUAL). Each player has a fixed maximum speed of
motion (SPEED), which may vary across players. Players may be able to
move and change direction throughout the game, or there may be actions
that prevent further motion (FREEZING\_ACTIONS).

Players take on one of some number of distinguishable identities
(NUM\_IDENTITIES). Players may select their identity of it may be
assigned to them (IS\_IDENTITY\_SELECTED). Players may be allowed to
move freely between identities (IS\_IDENTITY\_FLUID). Players may be
able to see the identity of others. Ability to see the identity of
others may depend on their position on the grid, the identity of the
player or the other player, or the network structure. Identities may be
transmissible based on spatial proximity or network structure.

Fig. 3. Sample colors that could serve as distinguishable identities.

Objects
~~~~~~~

The world may contain non-player objects that are immovable (e.g.,
walls) or movable (e.g., blocks).

Chatroom
~~~~~~~~

Players may be given a free-form chatroom that allows them to
communicate with others (IS\_CHATROOM). If there is a chatroom, players
may be able to communicate only with those who share an identity
(IS\_CHAT\_WITH\_OTHERS), are neighbors in their social network, or are
within some distance from the player (CHATROOM\_MIN\_DISTANCE).

Social network
~~~~~~~~~~~~~~

Players are situated in a social network that may determine who they can
see or chat with. Players may be able to rewire the network by forging
or breaking links.

Score
~~~~~

Players have a score that determines their payout in the game. A players
score rises and falls depending on their actions and those of others.
Players may receive points based on their location, proximity to others
in a network, random chance, and their interactions with others.

Actions
~~~~~~~

Players may be able to interact with other players. For example, players
may be able to transfer some or all of their score to others
(IS\_REWARD\_OTHERS, MAX\_REWARD\_TO\_OTHERS,
IS\_REWARD\_TO\_OTHERS\_ALL\_OR\_NONE), and this transference may be
limited by position, network structure, or identity.

Gameplay
~~~~~~~~

The game may have multiple rounds (NUM\_ROUNDS). Each round may last
until a particular outcome or for a given amount of time
(STOPPING\_RULE).

In-game questionnaire
~~~~~~~~~~~~~~~~~~~~~

At various points, the game may pause and players will be asked to
respond to the Dynamic Identity Fusion Index survey instrument as it
pertains to a particular identity. Players may also be asked to complete
a longer survey instrument. These survey instruments may also be
administered at the close of the game.

Metagame questionnaire
~~~~~~~~~~~~~~~~~~~~~~

Players will be asked various questions that exist outside the
Griduniverse. At the beginning of the study, they will be asked to
consent. At the end of the study, they will be asked to answer questions
about the difficulty of the game and their engagement with it.

Case study of a Gridworld, 1: the zombie game
---------------------------------------------

Over the past several years, a vibrant ecosystem of accessible web
technologies (e.g. WebSockets) has led to the proliferation of
interactive multiplayer online games. One such class of these games are
the so-called “io” games (http://iogames.space/), named for the
top-level domain on which they are often hosted (.io). In a typical io
game, a moderate number of people (10-100) compete for resources in a
fast-paced action game that lasts several minutes. The game is then
repeated. Our team recently found an io game with great relevance to the
problem of collective identity formation: braains.io.

Braains is a game in the popular zombie genre, inspired by horror films,
B movies, and literature. In the game, a set of 3-100 players are placed
in a random position in a multi-roomed house with a yard. Players have a
birds-eye view of a house and can control their position using their
keyboard. Before the game begins, all players are assigned the identity
of “human” and are free to roam about the house and move objects within
it. A timer at the top of the screen counts down until the game begins.
When the game begins, one player is selected at random and is reassigned
a new identity: “zombie”, taking on a new appearance. The player’s
identity determines the payoff structure of the game. Zombies are
rewarded for touching humans, who then become zombies. Humans are
rewarded for each second that they are not a zombie.

Braains is an interesting case study in human social behavior and
collective identity because of the rich array of behavior exhibited in
the game. For example, a social dilemma often arises during the initial
phase of the game. Players can collaborate to barricade rooms in such a
way that they are impenetrable by zombies (Fig. 4). Some rooms, however,
can only be successfully barricaded by someone outside the room. That
person pays the cost of helping but, by nature of the barricade, is
prevented from receiving its benefits. This is a Volunteer’s Dilemma, as
described by Schelling (1971). Later in the game, players begin to
become infected by zombies. At the moment of infection, a player’s
outward identity changes instantaneously. They are immediately
stigmatized by their group, who runs from them. How do perceptions of
identity change at this moment? When does a player come to feel a sense
of belonging to the zombies? There are many questions that can be asked.

A minimal version of Braains is one world in the Griduniverse.

Fig. 4. Screenshot of the Braains game. A group of humans act
collectively to prevent intrusion from zombies, who similarly take
collective action, but with opposite intentions.

Case study of a Gridworld, 1: the minimal group paradigm

The minimal group paradigm is an experimental paradigm from social
psychology that considers the minimal conditions needed to induce
in-group favoritism. The paradigm begins by assigning one of two
identities to a set of players. Identities may be assigned randomly
(e.g., red or blue as determined by a coin flip) or based on some
dimension along which people vary (e.g., odd or even birth month).
Players are then given the opportunity to divide a resource among pairs
of other players. The choices are manipulated to tease apart various
factors that may affect the resource allocation.

Exploring the Griduniverse
--------------------------

A vast number of games, social dilemmas, and experimental paradigms for
studying human social behavior can be expressed as worlds in the
Griduniverse.

Chicken
~~~~~~~

The game of chicken is one of brinkmanship. A pair of squares, one blue,
one yellow, each begin on the same row of a 2 × 20 grid, moving inward
toward each other. If they collide, both lose 10 points. If they pull to
the side, they each gain nothing. If one pulls to the side and the other
continues on course, the one who pulls to the side loses 5 and the one
who continues gains 5.

Fig. 5. Screenshot of chicken.

Schelling’s model of spatial segregation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spatial Voronoi game.
~~~~~~~~~~~~~~~~~~~~~

Matching pennies
~~~~~~~~~~~~~~~~

A pair of squares, one blue, one yellow, each begin on different rows of
a 2 x 20 grid, moving inward toward each other. If they collide, the
blue square wins. If they pass by each other, the yellow square wins.

Fig. 6. Screenshot of chicken.

Coordination game
~~~~~~~~~~~~~~~~~

A pair of squares, one blue, one yellow, each begin on different rows of
a 2 x 20 grid, moving inward toward each other. Each wins if they
collide and loses if they do not. Critically, they must choose whether
to move before seeing the other’s decision.

Battle of the sexes
~~~~~~~~~~~~~~~~~~~

Negotiation game
~~~~~~~~~~~~~~~~

Blotto game
~~~~~~~~~~~

(Time-based resource.)

Deadlock.
~~~~~~~~~

Prisoner’s dilemma
~~~~~~~~~~~~~~~~~~

Minority game
~~~~~~~~~~~~~

An odd number of players each choose one of two colors. Players in the
minority win. The game is iterated.

Snake
~~~~~

A single player hunts for food in an environment, growing in length by
one each time food is found. The player loses when the snake touches a
side wall or itself.

Dueling snakes
~~~~~~~~~~~~~~

A pair of players hunt for food in an environment, growing in length by
one each time food is found. A player loses when their snake touches a
side wall, itself, or the other snake.

Collective snake
~~~~~~~~~~~~~~~~

Schelling focal points
~~~~~~~~~~~~~~~~~~~~~~

Asch conformity experiments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Poetic generator
~~~~~~~~~~~~~~~~

Maze
~~~~

A single player navigates a maze, searching for an exit.

Reinforcement learning Gridworld
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Gridworlds that have been studied in reinforcement learning are
special cases of the Griduniverse.

Reduced Turing test
~~~~~~~~~~~~~~~~~~~

The participant plays a pair of identical Gridworld games, except that
in one the participant plays with a bot and in the other, the
participant plays with a human. At the end of the game, the participant
is asked to identify the bot.

Hedonic games
~~~~~~~~~~~~~

In a hedonic game, each of N players is assigned a unique identity and a
partial order over subsets of players that include the ego that
determines payoffs. these payoffs may conflict across players. Players
are given a chance to form coalitions. Payoff is determined by the
coalitions that are formed.

Tag
~~~

In the game of tag, one player is designated “it”. That player’s goal is
to touch another player, which transfers the identity of “it” to them.
The game continues indefinitely or for some set amount of time.

Irreversible tag
~~~~~~~~~~~~~~~~

In the game of irreversible tag, one player is designated “it”. That
player’s goal is to touch another player, who then joins the set of
people designated as “it”. The game ends when everyone has the identity
“it”. (This game is closely related to the zombie games.)

Blob tag
~~~~~~~~

In the game of blob tag, one player is designated “it”. That player’s
goal is to touch another player, who then joins the set of people
designated as “it”. Critically, all players with the identity “it” must
take collective action in order to move.


.. toctree::
    :maxdepth: 1
    :caption: Acknowledgements

    acknowledgments
