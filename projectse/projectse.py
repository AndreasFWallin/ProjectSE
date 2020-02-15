
""" Highest level and entrypoint of the ProjectSE / UU-game application """
import msvcrt

from projectse.player import *
from projectse.configuration import *
from projectse.game_manager import *
from projectse.tournament import *


class ProjectSE:
    def __init__(self):
        cb = ConfigurationBuilder()
        self.t = Tournament(cb)

    def menu_choice(self):
        if msvcrt.kbhit():
            key_hit = msvcrt.getch()
            if (key_hit == b't' or key_hit == b'T'):
                print("Get ready to rumble!!!")
                # TODO insert initialization of the tournament realm
            elif (key_hit == b'q' or key_hit == b'Q'):
                print("See you next time!")
            else:
                print("You pressed", key_hit,
                "This is not a valid key, press T or Q to start or quit")

    def start(self):
        print("Game started")
        
    def main_loop(self):
        pass





if __name__ == "__main__":
    ProjectSE().start()




def buttonListener():
    """
    A function that once called for will listen for a a T press or a Q press, when this occurs the 
    """
    while True:
