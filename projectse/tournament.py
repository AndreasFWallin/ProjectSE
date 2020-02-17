from random import randrange

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
        self.tournament_drawer = TournamentDrawer(self.list_players)
        self.round_num = 0
        self.most_wins = -1
        self.most_white_wins = -1
        self.all_matches = []
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
                self.tournament_drawer()
                print("         Test for updating tournament table. 1 and 3 won the game")
                self.tournament_drawer.updateTable(i,[1,3])
        self.stop_tournament()
            
            
    
    def print_round(self):
        for i in range(len(self.match_round)):
            print("In match", i+1, self.list_players[self.match_round[i][0]-1].name, "as white, versus",
            self.list_players[self.match_round[i][1]-1].name, " as black")

    def play_matches(self):
        for i in range(len(self.current_round.matches)):
            self.all_matches += self.current_round.unplayed_matches
            self.current_round.set_next_match()
            self.current_match = self.current_round.get_current_match()
            white = self.current_match.get_white_player()
            black = self.current_match.get_black_player()
            print("Now playing, ", self.current_match.get_white_player_name(),
            " as white, versus ", self.current_match.get_black_player_name(),
            "as black")
            print()
            self.current_match.winner = black
            if isinstance(white, AIPlayer) and isinstance(black, AIPlayer):
                print("AI VS AI, the winner will be determined by skill and luck")
                current_winner = self.aiplay(white, black)
                if current_winner == white:
                    current_winner.won_game_white()
                else:
                    current_winner.won_game() 
                self.current_match.winner = current_winner
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
<<<<<<< HEAD

    #If a 2 players are AI players the will be determined according to a probability
    def aiplay(self, player1,player2):
        if(isinstance(player1,AIPlayer) and isinstance(player2,AIPlayer)):
            if(player1.difficulty=="lo" and player2.difficulty=="lo"):
                if(randrange(100)<50):
                    return player1
                else:
                    return player2

            elif(player1.difficulty=="lo" and player2.difficulty=="mid"):
                if(randrange(100)<35):
                    return player1
                else:
                    return player2;
            elif(player1.difficulty=="lo"and player2.difficulty=="hi"):
                if(randrange(100)<15):
                    return player1
                else:
                    return player2
            elif(player1.difficulty=="mid"and player2.difficulty=="lo"):
                if(randrange(100)<35):
                    return player2
                else:
                    return player1
            elif(player1.difficulty=="mid"and player2.difficulty=="mid"):
                if(randrange(100)<50):
                    return player1
                else:
                    return player2;
            elif(player1.difficulty=="mid"and player2.difficulty=="hi"):
                if(randrange(100)<35):
                    return player1
                else:
                    return player2
            elif(player1.difficulty=="lo"and player2.difficulty=="mid"):
                if(randrange(100)<35):
                    return player1
                else:
                    return player2
            elif(player1.difficulty=="hi"and player2.difficulty=="lo"):
                if(randrange(100)<15):
                    return player2
                else:
                    return player1
            elif(player1.difficulty=="hi"and player2.difficulty=="mid"):
                if(randrange(100)<35):
                    return player2
                else:
                    return player1
            elif(player1.difficulty=="hi"and player2.difficulty=="hi"):
                if(randrange(100)<50):
                    return player1
                else:
                    return player2


=======
<<<<<<< HEAD


    #If a 2 players are AI players the will be determined according to a probability
    def aiplay(self, player1,player2):
        print(type(player1.difficulty), player2.difficulty)
        # if(isinstance(player1,AIPlayer) and isinstance(player2,AIPlayer)):
        if(player1.difficulty=="low" and player2.difficulty=="low"):
=======
#If a 2 players are AI players the will be determined according to a probability
def aiplay(player1,player2):
    if(isinstance(player1,AIPlayer) and isinstance(player2,AIPlayer)):
        if(player1.difficulty==1 and player2.difficulty==1):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<50):
                return player1;

            else:
                return player2;
        
<<<<<<< HEAD
        elif(player1.difficulty=="low" and player2.difficulty=="med"):
=======
        elif(player1.difficulty==1 and player2.difficulty==2):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<35):
                return player1;
            else:
<<<<<<< HEAD
                return player2
        elif(player1.difficulty=="low"and player2.difficulty=="hi"):
=======
                return player2;
        elif(player1.difficulty==1and player2.difficulty==3):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<15):
                return player1;
            else:
<<<<<<< HEAD
                return player2
        elif(player1.difficulty=="med"and player2.difficulty=="low"):
=======
                return player2;
        elif(player1.difficulty==2and player2.difficulty==1):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<35):
                return player2;
            else:
<<<<<<< HEAD
                return player1
        elif(player1.difficulty=="M" and player2.difficulty=="M"):
=======
                return player1;
        elif(player1.difficulty==2and player2.difficulty==2):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<50):
                return player1;
            else:
<<<<<<< HEAD
                return player2
        elif(player1.difficulty=="med"and player2.difficulty=="hi"):
=======
                return player2;
        elif(player1.difficulty==2and player2.difficulty==3):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<35):
                return player1;
            else:
<<<<<<< HEAD
                return player2
        elif(player1.difficulty=="low"and player2.difficulty=="med"):
=======
                return player2;
        elif(player1.difficulty==1and player2.difficulty==2):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<35):
                return player1;
            else:
<<<<<<< HEAD
                return player2
        elif(player1.difficulty=="hi"and player2.difficulty=="low"):
=======
                return player2;
        elif(player1.difficulty==3and player2.difficulty==1):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<15):
                return player2;
            else:
<<<<<<< HEAD
                return player1
        elif(player1.difficulty=="hi"and player2.difficulty=="med"):
=======
                return player1;
        elif(player1.difficulty==3and player2.difficulty==2):
>>>>>>> 7b37b11fa8950449c75a22b1c93ae6ca48945e85
            if(randrange(100)<35):
                return player2;
            else:
                return player1;
        elif(player1.difficulty==3and player2.difficulty==3):
            if(randrange(100)<50):
                return player1;
            else:
                return player2;
>>>>>>> master

    def tournament_drawer(self):
        self.all_matches += self.current_round.played_matches
        print(end = " "*9)
        for player in self.list_players:
            print(player.name, end = " "*(9-len(player.name)))
        print()
        for i, player1 in enumerate(self.list_players):
           
            print(player1.name, end = " "*(9-len(player1.name)))
            for j, player2 in enumerate(self.list_players):
                if i == j:
                    print("-", end = " "*8)
                else:
                    found = False
                    for match in self.all_matches:
                        if (player1 == match.white_player or player1 == match.black_player) and (player2 == match.white_player or player2 == match.black_player) and found == False:
                            print(match.winner.name, end = " "*(9-len(match.winner.name)))
                            found = True
                    if found == False:
                        print("*", end = " "*(8))
            print()


