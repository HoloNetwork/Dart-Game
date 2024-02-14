# Dart Game

Dart Game made with python. Consisting of Point, Player and DartGame class. 
Simulating a dart match by printing the result in the terminal.

## class Point: 

Returns the (x, y) coordinates.

Attributes:
- x (int): Coordinate x.
- y (int): Coordinate y.
- score (int): Applys distance formula to calculate score.

Methods:
- distance_from_zero(): Applys distance formula to calculate score.
- get_score(): Returns score.

##class Player: 

Returns a context string of; player_name, total_score, points.

Attributes:
- player_name (str): Player name.
- seed (int): Seed for random module initiate seed
- points (list): List of Points object

Methods:
- make_throw(): Context string of player name, coordinate and score.
- get_score(): Get last Points class score.
- get_total_score(): Get all Points class score.
- get_name(): Return player name.

## class DartGame: 

Simulates the DartGame

Attributes:
- player1 (class): Player 1; name, seed, points.
- player2 (class): Player 2; name, seed, points.
- max_score (int): Maximum score to reach.
- rounds (int): Amount of rounds played.

Methods:
- initialize(): Initializes Player 1 and Player 2 names.
- play_game(): Plays rounds until reaching max_score.
- congratulate_player(): Celebrates the winner.
