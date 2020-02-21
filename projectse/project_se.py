
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
        


    def tournament_start_choice(self):
        """ Get user input to determine if to start
        new tournament (True) or exit (False)"""
        """
        A function that once called for will listen for a a T press or a Q press, when this occurs the 
        """
        print("Welcome to the UU-game press 'T' to start or 'Q' to quit")
        while True:
            key_hit = input()
            if (key_hit == 'T'):
                return True
            elif (key_hit == 'Q'):
                print("See you next time!")
                return False
            else:
                print("You pressed", key_hit,
                "This is not a valid key, press T or Q to start or quit")

    def start(self):
        print("Application started")
        choice = self.tournament_start_choice()
        if choice:
            self.cb.query_players()
            
        if choice:
            self.main_loop()
        self.exit()
        
    def main_loop(self):
        print("Get ready to rumble!!!")
        self.t = Tournament(self.cb.cfg)
        self.t.start_tournament()

    def exit(self):
        print("Game exited")


if __name__ == "__main__":
    ProjectSE().start()
