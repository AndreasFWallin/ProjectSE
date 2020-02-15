from tournament_scheduler import *
class Tournament:
    """ Tournament is responsible for handling a round-robin tournament for a two player game based on a collection of
        players (which players and their properties is decided elsewhere). It keeps track of current game, next game, who won etc. """
    def __init__(self, config):
        self.config = config
        # Below the players are put in a list first as strings and AIs are after encoded as ints
        self.list_players = config.players + list(range(1, config.num_ai))
        self.num_players = len(self.list_players)
        self.wins = [0]*self.num_players # Array for keeping track of the wins
        self.tournament_scheduler = TournamentScheduler(self.num_players)
        self.round_num = 0


    def start_tournament(self):
        """

        """
        for i in range(self.num_players):
            self.current_round = self.tournament_scheduler.get_round(i+1)
            print_round()
            
    
    def print_round(self):
        print("This is round number, ", self.round_num)
        for i in range(len(self.current_round)):
            print("In match", self.list_players[i], self.current_round[i][0], "as white, versus",
            self.current_round[i][1], " as black")


    def stop_tournament(self):
        pass
