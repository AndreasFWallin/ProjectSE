
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

class MockPlatform:

    def initialize(self):
        return ""

    def get_menu_choice(self):
        return "Singleplayer"


class ProjectSE:
    def __init__(self):
        self.cb = ConfigurationBuilder()
        self.platform = MockPlatform()
        self.game_mgr = GameManager()
        #TODO: wait with this, if no connection we cant play
        # self.game_mgr.connect()

    def intro_menu_choice(self):
        """ Get user input to determine if to start
        new tournament, singleplayer or exit"""
        print("Welcome to the UU-game press 'T' to start tournament, 'S' for single or 'Q' to quit")
        while True:
            key_hit = input()
            if (key_hit == 'T'):
                return "Tournament"
            elif (key_hit == 'S'):
                print("Singleplayer!")
                return "Single"
            elif (key_hit == 'Q'):
                print("See you next time!")
                return "Quit"
            else:
                print("You pressed", key_hit,
                "This is not a valid key, press T or Q to start or quit")

    def init(self):
        print("Application started")
        #choice = self.platform.get_menu_choice()
        choice = self.intro_menu_choice()

        while choice != "Quit":
            if choice == "Tournament":
                players_cfg = self.cb.query_settings()
                tournament = Tournament(players_cfg)
                self.play_tournament(tournament)
            elif choice == "Single":
                self.play_match()
            else:
                raise NotImplementedError("No such choice")
            choice = self.platform.get_menu_choice()

        self.exit()

    def setup_platform(self, match):
        """ Interface to Platform to set type of players and names """
        self.platform.setup(match)

    def play_tournament(self, tournament):
        round = tournament.get_next_round()
        while round is not None:
            match = tournament.get_next_match()
            while match is not None:
                # AI vs AI is determined by tournament and not actually played.
                if match.only_ai():
                    winner = tournament.aiplay(match)
                else:
                    winner = self.play_match(match)
                tournament.set_result(winner)
                match = tournament.get_next_match()
            round = tournament.get_next_round()
        print("Tournament completed")

    def play_match(self, match) -> Player:
        """
        Used to play a game by first initializing the platform with
        information about the match and then playing until the match is finished.
        Winning player is returned, if draw None is returned.
        """
        self.setup_platform(match)
        board_state = BoardState()
        while not board_state.is_finished():
            if board_state.ai_turn():
                board_state = self.game_mgr.make_move(board_state)
            board_state = self.platform.play(board_state)

        winner = board_state.get_winner()
        return winner


    def main_loop(self):
        print("Get ready to rumble!!!")

    def exit(self):
        print("Game exited")


if __name__ == "__main__":
    ProjectSE().init()
