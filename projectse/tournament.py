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
        self.tournamentdrawer = TournamentDrawer(self.list_players)
        self.round_num = 0
        self.match_num = 0

        self.rounds = self.get_model_as_rounds()


    def get_model_as_rounds(self):
        """ Creates a list of rounds containing all the matches """
        round_list = []
        num_players = len(self.list_players)
        scheduler = TournamentScheduler(num_players)
        for round in scheduler.schedule:
            r = Round()
            for white_inx, black_inx in round:
                # List_players is 0 indexed but the indexes from the scheduler is 1 indexed.
                match = Match(self.list_players[white_inx-1],self.list_players[black_inx-1])
                r.add_match(match)
            round_list.append(r)
        return round_list

    def get_current_match(self):
        return self.get_current_round().get_current_match()

    def get_current_round(self):
        return self.rounds[self.round_num]

    def get_next_round(self):
        if self.round_num < len(self.rounds)-1:
            self.round_num+=1
            return self.get_current_round()
        else:
            return None

    def get_next_match(self):
        print("Press enter to play game, press 'Q' to quit")
        inp = input()
        if (inp ==  'Q'):
            print("Game quit.")
            exit()
        next_match = self.get_current_round().get_next_match()
        return next_match

    def set_result(self, current_winner):
        #TODO: Most of this should be done in Match class for cohesions sake
        is_draw = False
        white = self.get_current_match().get_white_player()
        white.played_white()
        black = self.get_current_match().get_black_player()
        if current_winner == white:
            current_winner.won_game_white()
            self.get_current_match().loser = black
        elif current_winner == black:
            current_winner.won_game()
            self.get_current_match().loser = white
        else:
            is_draw = True
            white.tie_game()
            black.tie_game()
            
        self.get_current_match().winner = current_winner
        print(self.get_current_match().winner.name, "won the game. \n \n")
        self.tournamentdrawer.updateTable(self.get_current_match().winner,
                                          self.get_current_match().loser,
                                          is_draw)

    """
    def start_tournament(self):
        
        Here the tournament is started and played.
       

        for i in range(self.num_players):
            self.matches_in_round = self.tournament_scheduler.get_round(i+1)
            if self.matches_in_round != None:  # Odd # players 
                current_round = Round(self.matches_in_round, self.config)
                print("This is round number, ", i+1)
                self.print_round()
                self.play_matches(current_round)
                self.tournamentdrawer.drawResultTable()
        self.stop_tournament()
     """
            
    
    def print_round(self):
        for num, match in enumerate(self.get_current_round().matches):
            print("In match", num+1, match.get_white_player_name(), "as white, versus",
            match.get_black_player_name(), " as black")


    def stop_tournament(self):
        """
        The end of tournament, where the winner is announced and
        the tournament can be replayed if input is given 
        """
        most_wins = -1
        winner = None

        for player in self.list_players:
            print(player.name, player.wins)
            if player.wins > most_wins:
                winner = player
                most_wins = player.wins
            elif player.wins == most_wins: # Player that won the match is tournament winner
                # print("Head to head", player, self.winner)
                match = self.find_match(self.winner, player)
                if match.winner == player:
                   # print(match.winner.name)
                   winner == player
                   most_wins = player.wins
                elif match.winner== None:
                    if winner.white_played < player.white_played:
                        winner=player
                    
        print("The winner is ", winner.name,   " with ", winner.wins, " wins")

    def ask_retry(self):
        print("Do you want to play again with the same setup, input 'R' or, input any other button to exit:")
        inp = input()
        if inp == "R":
            return True
        else:
            return False

    def aiplay(self, match):
        """
        If a 2 players are AI players the outcome
        will be determined according to a probability
        """
        player1 = match.get_white_player()
        player2 = match.get_black_player()

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

    def get_all_matches(self):
        a = []
        for round in self.rounds:
            for matches in round.get_matches():
                a.append(matches)
        return a

    def find_match(self, player1, player2):
        """
        Finds the match that had player1 and player2  and returns it
        """
        for match in self.get_all_matches():
            if (player1 == match.white_player or player1 == match.black_player) and (player2 == match.white_player or player2 == match.black_player):
                return match
        print("ERROR, MATCH NOT FOUND THIS SHOULD ONLY BE USED AT THE END")
