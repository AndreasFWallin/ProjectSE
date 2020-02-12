from projectse.player import *
from enum import Enum
""" Configuration module from which user-input will define properties for a tournament"""
AIDifficulty = Enum("AIDifficulty", "low med hi")

class Configuration:
    """ Configuration object to be send to configure the tournament """
    def __init__(self):
        self.num_ai=0
        self.players=[]

    def set_players(self, players):
        self.players=players

class ConfigurationBuilder:
    """ Responsible for collecting info while creating the Configuration object """
    def __init__(self, cfg: Configuration):
        self.cfg = cfg

    def get_input(self, msg):
        return input(msg)

    def get_number_input(self, msg, min, max):
        err_msg = "\nError: Input must be an integer between {}-{} ".format(min,max)
        print("get num input")
        while True:
            try:
                x = int(self.get_input(msg))
                print("num inp:"+str(x))
                if x in range(min, max+1):
                    return x
                else:
                    raise ValueError

            except ValueError:
                self.print_out(err_msg)

    def print_out(self, msg):
        print(msg)

    def get_char_input(self, msg, chars):
        ok = False
        err_msg = "\nError: Input must be one of {} ".format(str(chars))
        while not ok:
            x = self.get_input(msg)
            if x in chars:
                ok = True
                return x
            else:
                self.print_out(err_msg)

    def parse_difficulty(self, diff_str):
        diffmap = {"H":AIDifficulty.hi, "L":AIDifficulty.low, "M":AIDifficulty.med}
        value = diffmap.get(diff_str)
        print("diff str key:{} value:{}".format(diff_str,value))

        return value

    def query_players(self):
        """ menu for dealing with adding all the players to the configuration """
        """ First number of players, then number of human players, and then difficulty 
            for each AI-player """
        max_players = 99
        player_list = []
        self.print_out("= Configuration. Player setup =")
        total_players = self.get_number_input("Select total number of players:",1,max_players)
        num_ai_player = self.get_number_input("Select number of AI players:",0,total_players)
        for ai_player in range(num_ai_player):
            diff = self.get_char_input("Set difficulty for AI player #{}".format(ai_player+1), ["H", "M", "L"])
            player_list.append(AIPlayer("AIPlayer"+str(ai_player+1), self.parse_difficulty(diff)))

        for human_player in range(total_players-num_ai_player):
            name = self.get_input("Set name for Player#{}".format(human_player+1))
            player_list.append(Player(name))

        self.configure_players(player_list)


    def configure_players(self,player_list):
        self.cfg.add_players(player_list)

