
from projectse.player import *
""" Configuration module from which user-input will define properties for a tournament"""

class Configuration:
    """ Configuration object to be send to configure the tournament """
    def __init__(self):
        self.num_ai=0
        self.players=[]

    def set_players(self, players):
        self.players=players


class ConfigurationBuilder:
    """ Responsible for collecting info while creating the Configuration object """
    def __init__(self):
        self.cfg = Configuration()

    def get_input(self, msg):
        return input(msg)

    def parse_platform_singleplay_to_cfg(self,setting_obj):
        """ Converts settingsobject to
        """


    def get_number_input(self, msg, min, max):
        err_msg = "\nError: Input must be an integer between {}-{} ".format(min,max)
        #print("get num input")
        while True:
            try:
                x = int(self.get_input(msg))
                #print("num inp:"+str(x))
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
        #print("diff str key:{} value:{}".format(diff_str,value))

        return value

    def query_settings(self):
        """ menu for dealing with adding all the players to the configuration """
        """ First number of players, then number of human players, and then difficulty 
            for each AI-player """
        max_players = 8
        player_list = []
        name_list = []
        self.print_out("= Configuration. Player setup =")
        total_players = self.get_number_input("Select total number of players, between 3 and 8: ", 3, max_players)
        #There needs to be atleast one human player
        num_ai_player = self.get_number_input("Select number of AI players: ", 0, total_players-1)
        if num_ai_player > 0:
            print("To select High difficulty use: 'H'. Medium: 'M'. Low: 'L' ")
        for ai_player in range(num_ai_player):
            diff = self.get_char_input("Set difficulty for AI player,#{} ".format(ai_player+1), ["H", "M", "L"])
            player_list.append(AIPlayer("AIPlayer"+str(ai_player+1)+diff, self.parse_difficulty(diff)))
        print("The name(s) input needs to be unique and no longer than 7 characters.")
        for human_player in range(total_players-num_ai_player):
            name = self.get_input("Set name for Player#{}, ".format(human_player+1))
            valid_name = self.valid_name(name, name_list, human_player)
            if valid_name:
                name = valid_name
            name_list.append(name)
            player_list.append(Player(name))
        self.configure_players(player_list)

        return self.cfg

    def configure_players(self,player_list):
        self.cfg.set_players(player_list)

    def valid_name(self, name, name_list, human_player):
        """
        Makes sure the name input is not too long and unique
        """
        if name in name_list:
            while True:
                print("The name ", name, " is not unique, please enter a new one")
                name = self.get_input("Set name for Player#{}".format(human_player + 1))
                if name not in name_list:
                    return name
        if len(name) > 7:
            while True:
                print("The name ", name, " is too long, please enter a new one that is shorter than 7 characters")
                name = self.get_input("Set name for Player#{}".format(human_player + 1))
                if name not in name_list:
                    return name