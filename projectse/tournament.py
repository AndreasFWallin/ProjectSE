from random import randrange

from projectse.configuration import *
from projectse.player import *
from projectse.tournament_scheduler import *
from projectse.round import *
from projectse.tournament_drawer import *


class Tournament:
    """ Tournament is responsible for handling a round-robin tournament for a two player game based on a collection of
        players (which players and their properties is decided elsewhere). It keeps track of current game, next game, who won etc. """
    def __init__(self, config):
        self.config = config
        # Below the players are put in a list first as strings and AIs are after encoded as ints
        self.list_players = config.players
        self.num_players = len(self.list_players)
        self.tournament_scheduler = TournamentScheduler(self.num_players)
        self.tournamentdrawer = TournamentDrawer(self.list_players)
        self.round_num = 0
        self.most_wins = -1
        self.most_white_wins = -1
        self.all_matches = []
        self.matches_in_round = None
        self.match = None
        self.winner = None



    def start_tournament(self):
        """
        Here the tournament is started and played.
        """

        for i in range(self.num_players):
            self.matches_in_round = self.tournament_scheduler.get_round(i+1)
            if self.matches_in_round != None:  # Odd # players 
                current_round = Round(self.matches_in_round, self.config)
                print("This is round number, ", i+1)
                self.print_round()
                self.play_matches(current_round)
                self.tournament_drawer(current_round)
                # print("         Test for updating tournament table. 1 and 3 won the game")
                # self.tournamentdrawer.updateTable(i,[1,3])
        self.stop_tournament()
            
            
    
    def print_round(self):
        for i in range(len(self.matches_in_round)):
            print("In match", i+1, self.list_players[self.matches_in_round[i][0]-1].name, "as white, versus",
            self.list_players[self.matches_in_round[i][1]-1].name, " as black")

    def play_matches(self, current_round):
        """
        Here the actual matches (1v1) are played in a round
        """
        for i in range(len(current_round.matches)):
            print("Press enter to play game, press 'Q' to quit")
            inp = input()
            if (inp ==  'Q'):
                print("Game quit.")
                exit()
            self.all_matches += current_round.unplayed_matches
            current_round.set_next_match()
            current_match = current_round.get_current_match()
            white = current_match.get_white_player()
            black = current_match.get_black_player()
            print("Now playing, ", current_match.get_white_player_name(),
            " as white, versus ", current_match.get_black_player_name(),
            "as black")
            print()
            

            if isinstance(white, AIPlayer) and isinstance(black, AIPlayer):
                print("AI VS AI, the winner will be determined by skill and luck")
                current_winner = self.aiplay(white, black)
                if current_winner == white:
                    current_winner.won_game_white()
                else:
                    current_winner.won_game() 
                current_match.winner = current_winner
            else: 
                print("PLACEHOLDER FOR ACTUAL GAME")
                # TODO add the actual game where the match is being played
                current_winner = black  # CHANGE WHEN ACTUAL GAMES IS ADDED
                if current_winner == white:
                    current_winner.won_game_white()
                else:
                    current_winner.won_game() 
                current_match.winner = current_winner
            print(current_match.winner.name, "won the game. \n \n")

    def stop_tournament(self):
        """
        The end of tournament, where the winner is announced and
        the tournament can be replayed if input is given 
        """
        for player in self.list_players:
            print(player.name, player.wins)
            if player.wins > self.most_wins:
                self.winner = player
                self.most_wins = player.wins
            elif player.wins == self.most_wins: # Player that won the match is tournament winner
                # print("Head to head", player, self.winner)
                match = self.find_match(self.winner, player)
                if match.winner == player:
                   # print(match.winner.name)
                   self.winner == player
                   self.most_wins = player.wins
        print("The winner is ", self.winner.name, " with ", self.winner.wins, " wins")

        print("Do you want to play again with the same setup, input 'R' or, input any other button to exit:")
        inp = input()
        if (inp == "R"):
            self.start_tournament()
            print("Reinstating the tournament")

    def aiplay(self, player1, player2):
        """
        If a 2 players are AI players the will be determined according to a probability
        """
    
        if(player1.difficulty==AIDifficulty.low and player2.difficulty==AIDifficulty.low):
            if(randrange(100)<50):
                return player1
            else:
                return player2

        elif(player1.difficulty==AIDifficulty.low and player2.difficulty==AIDifficulty.med):
            if(randrange(100)<35):
                return player1
            else:
                return player2
        elif(player1.difficulty==AIDifficulty.low and player2.difficulty==AIDifficulty.hi):
            if(randrange(100)<15):
                return player1
            else:
                return player2
        elif(player1.difficulty==AIDifficulty.med and player2.difficulty==AIDifficulty.low):
            if(randrange(100)<35):
                return player2
            else:
                return player1
        elif(player1.difficulty==AIDifficulty.med and player2.difficulty==AIDifficulty.med):
            if(randrange(100)<50):
                return player1
            else:
                return player2
        elif(player1.difficulty==AIDifficulty.med and player2.difficulty==AIDifficulty.hi):
            if(randrange(100)<35):
                return player1
            else:
                return player2
        elif(player1.difficulty==AIDifficulty.low and player2.difficulty==AIDifficulty.med):
            if(randrange(100)<35):
                return player1
            else:
                return player2
        elif(player1.difficulty==AIDifficulty.hi and player2.difficulty==AIDifficulty.low):
            if(randrange(100)<15):
                return player2
            else:
                return player1
        elif(player1.difficulty==AIDifficulty.hi and player2.difficulty==AIDifficulty.med):
            if(randrange(100)<35):
                return player2
            else:
                return player1
        elif(player1.difficulty==AIDifficulty.hi and player2.difficulty==AIDifficulty.hi):
            if(randrange(100)<50):
                return player1
            else:
                return player2

    def find_match(self, player1, player2):
        """
        Finds the match that had player1 and player2  and returns it
        """
        for match in self.all_matches:
            if (player1 == match.white_player or player1 == match.black_player) and (player2 == match.white_player or player2 == match.black_player):
                return match
        print("ERROR, MATCH NOT FOUND THIS SHOULD ONLY BE USED AT THE END")





    def tournament_drawer(self, current_round):
        """
        Not in use, prints a table try it by uncommenting in start tournament
        """
        print("TBD = To Be Decided")
        self.all_matches += current_round.played_matches
        print(end=" " * 15)
        for player in self.list_players:
            print(player.name, end=" " * (15 - len(player.name)))
        print()
        for i, player1 in enumerate(self.list_players):

            print(player1.name, end=" " * (15 - len(player1.name)))
            for j, player2 in enumerate(self.list_players):
                if i == j:
                    print("-", end=" " * 14)
                else:
                    found = False
                    for match in self.all_matches:
                        if (player1 == match.white_player or player1 == match.black_player) and (
                                player2 == match.white_player or player2 == match.black_player) and found == False:
                            print(match.winner.name, end=" " * (15 - len(match.winner.name)))
                            found = True
                    if found == False:
                        print("TBD", end=" " * (12))
            print()
        