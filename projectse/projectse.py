
""" Highest level and entrypoint of the ProjectSE / UU-game application """

from projectse.player import *
from projectse.configuration import *
from projectse.engine_manager import *
from projectse.tournament import *


class ProjectSE:

    def start(self):
        Configuration()
        print("Game started")





if __name__ == "__main__":
    ProjectSE().start()