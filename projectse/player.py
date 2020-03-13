from enum import Enum

AIDifficulty = Enum("AIDifficulty", "low med hi")

class Player:
    """ Human Player for the UU-game"""
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.white_wins = 0
        self.result = False
        self.white_played = 0
    def won_game(self):
        self.wins += 1
    def tie_game(self):
        self.wins +=0.5
        
    def won_game_white(self):
        self.wins += 1
        self.white_wins += 1
    
    def played_white(self):
        self.white_played +=1
    
    def is_ai(self):
        return False

class AIPlayer(Player):
    """ Player controlled by a computer """
    def __init__(self, name, difficulty):
        self.difficulty = difficulty
        super().__init__(name)

    def is_ai(self):
        return True
