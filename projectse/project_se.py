
""" Highest level and entrypoint of the ProjectSE / UU-game application """
import os
import sys
p = os.path.abspath("")
p.encode('unicode_escape')
print(p)
sys.path.insert(0, p)
from player import *
from configuration import *
from game_manager import *
from tournament import *


class ProjectSE:
    def __init__(self):
        self.cb = ConfigurationBuilder()
        self.platform = None
        


    def intro_menu_choice(self):
        """ Get user input to determine if to start
        new tournament (True) or exit (False)"""
        """
        A function that once called for will listen for a a T press or a Q press, when this occurs the 
        """
        print("Welcome to the UU-game press 'T' to start or 'Q' to quit")
        while True:
            key_hit = input()
            if (key_hit == 'T'):
                return "Tournament"
            elif (key_hit == 'Q'):
                print("See you next time!")
                return "Quit"
            else:
                print("You pressed", key_hit,
                "This is not a valid key, press T or Q to start or quit")

    def init(self):
        print("Application started")
        choice = self.intro_menu_choice()
        if choice == "Tournament":
            # self.cb.query_players()

            self.start_platform()
        elif choice == "Quit":
            self.exit()

    def start_platform(self):
        #TODO
        # cfg = self.platform.getconfig()
        # if isinstance(cfg, TournamentConfiguration())
        #   self.run_tournament(cfg)
        # elif isinstance(cfg, SinglePlayConfiguration())
        #   match = self.create_match(cfg)
        #   self.play_match(match)
        # match_result = self.run_platform()

    def run_tournament(self, cfg):
        # TODO
        # t = Tournament(cfg)
        # for match in t.getRound(1)
        #   self.play_match(match)
        #

    def create_match(self, cfg) -> Match:
        # TODO
        #return Match(Player(cfg.blabla),AIPlayer(cfg.diff))

    def play_match(self, match) -> Match:

        response = None
        self.platform.init(match)
            while not isinstance(response, Match):

                board_state = self.platform.player_move()
                new_board_state = self.game_manager.send_n_receive(board_state)
                self.platform.update_board(new_board_state)
                # if check if there was a winner
                # Evaluate the response, either we send it to the gameengine
                # Or the match is finished and we return the match as a result

        return response

    def run_platform(self):
        #TODO
        # boardState = self.platform.getMove()
        # if boardState is None:
        #


        
    def main_loop(self):
        print("Get ready to rumble!!!")
        self.t = Tournament(self.cb.cfg)
        self.t.start_tournament()

    def exit(self):
        print("Game exited")


if __name__ == "__main__":
    ProjectSE().init()
