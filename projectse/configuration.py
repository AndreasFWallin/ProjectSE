from projectse.player import *

""" Configuration module from which user-input will define properties for a tournament"""
class Configuration:
    """ Configuration object to be send to configure the tournament """
    def __init__(self):
        self.num_ai=0
        self.players=[]

    def add_player(self, player):
        self.players.append(player)

class ConfigurationBuilder:
    """ Responsible for collecting info while creating the Configuration object """
    def __init__(self, cfg: Configuration):
        self.cfg = cfg

    def get_input(self, msg):
        return input(msg)

    def print_out(self, msg):
        print(msg)

    def input_num_AIs(self):
        ok = False
        x=0
        while not ok:
            try:
                x = int(self.get_input("How many AI players? "))
                ok = True
                for a in range(x):
                    self.cfg.add_player(AIPlayer())

            except ValueError:
                self.print_out("\nError: Input must be an integer\n")
                #x = int(self.get_input("How many AI players? "))
