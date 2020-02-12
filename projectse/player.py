class Player:
    """ Human Player for the UU-game"""
    def __init__(self,name):
        self.name = name

class AIPlayer(Player):
    """ Player controlled by a computer """
    def __init__(self, name, difficulty):
        self.difficulty = difficulty
        super().__init__(name)