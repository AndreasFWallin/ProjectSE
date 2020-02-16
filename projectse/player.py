class Player:
    """ Human Player for the UU-game"""
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.white_wins = 0
        self.result=False;
    def won_game(self):
        self.wins += 1
    def won_game_white(self):
        self.wins += 1
        self.white_wins += 1

        
        
class AIPlayer(Player):
    """ Player controlled by a computer """
    def __init__(self, name, difficulty):
        self.difficulty = difficulty
        super().__init__(name)
