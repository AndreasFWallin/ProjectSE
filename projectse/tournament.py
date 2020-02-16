from projectse.player import *
from projectse.tournament_scheduler import *
from round import *
class Tournament:
    """ Tournament is responsible for handling a round-robin tournament for a two player game based on a collection of
        players (which players and their properties is decided elsewhere). It keeps track of current game, next game, who won etc. """
    def __init__(self, config):
        self.config = config
        # Below the players are put in a list first as strings and AIs are after encoded as ints
        self.list_players = config.players
        self.num_players = len(self.list_players)
        self.tournament_scheduler = TournamentScheduler(self.num_players)
        self.round_num = 0
        self.most_wins = 0
        self.most_white_wins = -1
        self.match_round = None
        self.current_round = None
        self.current_match = None
        self.match = None
        self.winner = None
        


    def start_tournament(self):
        """

        """
        for i in range(self.num_players):
            self.match_round = self.tournament_scheduler.get_round(i+1)
            if self.match_round != None: # 
                self.current_round = Round(self.match_round, self.config)
                print("This is round number, ", i+1)
                self.print_round()
                self.play_matches()
        self.stop_tournament()
            
            
    
    def print_round(self):
        for i in range(len(self.match_round)):
            print("In match", i+1, self.list_players[self.match_round[i][0]-1].name, "as white, versus",
            self.list_players[self.match_round[i][1]-1].name, " as black")

    def play_matches(self):
        for i in range(len(self.current_round.matches)):
            self.current_round.set_next_match()
            self.current_match = self.current_round.get_current_match()
            white = self.current_match.get_white_player()
            black = self.current_match.get_black_player()
            print("Now playing, ", self.current_match.get_white_player_name(),
            " as white, versus ", self.current_match.get_black_player_name(),
            "as black")
            if isinstance(white, AIPlayer) and isinstance(black, AIPlayer):
                print("AI VS AI, the winner will be determined by skill and luck")
                # TODO add AI vs AI random selector
            else: 
                print("PLACEHOLDER FOR ACTUAL GAME")
                # TODO add the actual game where the match is being played
                if white.name == "winner":
                    white.won_game_white()
             


    def stop_tournament(self):
        for player in self.list_players:
            if player.wins > self.most_wins and player.white_wins > self.most_white_wins:
                self.winner = player
        print("The winner is ", self.winner.name, " with ", self.winner.wins, " wins")

        print("Do you want to play again with the same setup, input 'R' or, input any other button to exit:")
        inp = input()
        if (inp == "r" or inp == "R"):
            self.start_tournament()
            print("Reinstating the tournament")

