
""" Highest level and entrypoint of the ProjectSE / UU-game application """

from projectse.player import *
from projectse.configuration import *
from projectse.game_manager import *
from projectse.tournament import *


class ProjectSE:
    def __init__(self):
        cb = ConfigurationBuilder()
        self.t = Tournament(cb)

    def start(self):
        print("Game started")
        
    def main_loop(self):
        pass





if __name__ == "__main__":
    ProjectSE().start()