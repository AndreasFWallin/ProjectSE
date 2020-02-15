
""" Highest level and entrypoint of the ProjectSE / UU-game application """
import msvcrt

from projectse.player import *
from projectse.configuration import *
from projectse.game_manager import *
from projectse.tournament import *

class ProjectSE:
    def __init__(self):
        self.cb = ConfigurationBuilder()
        self.t = Tournament()

    def tournament_start_choice(self):
        """ Get user input to determine if to start
        new tournament (True) or exit (False)"""
        """
        A function that once called for will listen for a a T press or a Q press, when this occurs the 
        """
        while True:
            if msvcrt.kbhit():
                key_hit = msvcrt.getch()
                if (key_hit == b't' or key_hit == b'T'):
                    print("Get ready to rumble!!!")
                    return True
                elif (key_hit == b'q' or key_hit == b'Q'):
                    print("See you next time!")
                    return False
                else:
                    print("You pressed", key_hit,
                    "This is not a valid key, press T or Q to start or quit")

    def start(self):
        print("Application started")
        #TODO: keyhit doesnt work
        if True:
            self.cb.query_players()
        if self.tournament_start_choice() == True:
            self.main_loop()
        self.exit()
        
    def main_loop(self):
        print("PLACEHOLDER FOR GAME")

    def exit(self):
        print("Game exited")


if __name__ == "__main__":
    ProjectSE().start()
