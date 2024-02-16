import math
import random

class Point:
    """Returns the (x, y) coordinates.
        Attributes:
        - x (int): Coordinate x.
        - y (int): Coordinate y.
        - score (int): Applys distance formula to calculate score.

        Methods:
        - distance_from_zero(): Applys distance formula to calculate score.
        - get_score(): Returns score.
    """
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.score = self.distance_from_zero()

    def distance_from_zero(self):
        x = self.coord_x
        y = self.coord_y
        
        distance = math.sqrt((x ** 2) + (y ** 2))
        
        if distance <= 1:
            return 100
        elif 1 < distance <= 2:
            return 50
        elif 2 < distance <= 3:
            return 20
        elif 3 < distance <= 4:
            return 10
        return 0

    def get_score(self):
        return self.score

    def __str__(self):
        return f"({self.coord_x}, {self.coord_y})"

class Player:
    """Returns a context string of; player_name, total_score, points.
        Attributes:
        - player_name (str): Player name.
        - seed (int): Seed for random module initiate seed
        - points (list): List of Points object

        Methods:
        - make_throw(): Context string of player name, coordinate and score.
        - get_score(): Get last Points class score.
        - get_total_score(): Get all Points class score.
        - get_name(): Return player name.
    """
    def __init__(self, name, seed):
        self.player_name = name
        self.seed = seed
        random.seed(self.seed)
        self.points = []
        
    def make_throw(self):
        player_name = self.player_name
        points = self.points
        
        x = random.randrange(-5, 6)
        y = random.randrange(-5, 6)
        p = Point(x, y)
        points.append(p)

        string = f"{player_name}: The score for a dart throw at position "
        string += f"{points[-1]} is {points[-1].get_score()}."
        
        print(string)
        return string
    
    def get_score(self):
        return self.points[-1].get_score()

    def get_total_score(self):
        total_score = 0
        
        for i in range(len(self.points)):
            total_score += self.points[i].get_score()

        return total_score

    def get_name(self):
        return self.player_name

    def __str__(self):
        player_name = self.player_name
        total_score = self.get_total_score()
        points = self.points
        
        start_string = f"{player_name}'s total score is {total_score}.\n"
        
        for i in range(len(self.points)):
            start_string += f"The score for a dart throw at position "
            start_string += f"{points[i]} is {points[i].get_score()}.\n"

        return start_string.rstrip()
    
class DartGame:
    """
        Attributes:
        - player1 (class): Player 1; name, seed, points.
        - player2 (class): Player 2; name, seed, points.
        - max_score (int): Maximum score to reach.
        - rounds (int): Amount of rounds past.

        Methods:
        - initialize(): Player 1 and player 2 names
        - play_game(): Plays rounds until reaching max_score
        - congratulate_player(): Celebrate winner
    """
    def __init__(self, seed=30, max_score=51):
        player1_name, player2_name = self.initialize()
        self.player1 = Player(player1_name, seed)
        self.player2 = Player(player2_name, seed)
        self.max_score = max_score
        self.rounds = 0

    def initialize(self):
        print("***********************************************")
        print("Welcome to the simplified dart game simulation!")
        print("***********************************************")

        player1_name = ''
        while player1_name == '':
            player1_name = input("Enter player1 name: ")
            
        player2_name = ''
        while player2_name == '':
            player2_name = input("Enter player2 name: ")

        print("")
        return player1_name, player2_name

    def play_game(self):
        player1 = self.player1
        player2 = self.player2
        max_score = self.max_score
        
        while (self.player1.get_total_score() < max_score
               and self.player2.get_total_score() < max_score):
            player1.make_throw()
            player2.make_throw()
            self.rounds += 1

    def congratulate_player(self):
        player1_total_score = self.player1.get_total_score()
        player2_total_score = self.player2.get_total_score()
        player1_name = self.player1.get_name()
        player2_name = self.player2.get_name()

        congratulate_string = "Congratulations! The winner is "
        
        if player1_total_score > player2_total_score:
            congratulate_string += f"{player1_name}."
            bar = "*" * len(congratulate_string)
            print(f"{bar}\n {congratulate_string}\n {bar}")


        elif player1_total_score < player2_total_score:
            congratulate_string += f"{player2_name}."
            bar = "*" * len(congratulate_string)
            print(f"{bar}\n {congratulate_string}\n {bar}")
            
        else:
            print("***********")
            print("It's a tie!")
            print("***********")

        print(f"The number of rounds required is {self.rounds}.")
        print(f"The total score of {player1_name} is {player1_total_score}.")
        print(f"The total score of {player2_name} is {player2_total_score}.")
      
