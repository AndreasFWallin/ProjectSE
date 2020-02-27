
class TournamentDrawer:
    def __init__(self, list_players):
        self.list_players = list_players
        n = len(self.list_players)
        self.results = [["*"] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.results[i][j] = "x"


    def drawResultTable(self):
        """ Prints the data stored in the 2D-array self.results(contains only 1/*/0 etc)
         together with the player names in the list self.list_players """
        col_length = 10
        division_rows="|-" + ("-"*(col_length+2) + "|")*(len(self.list_players) + 2)


        #Column headers
        print("\t\tTournament Results")
        print("\tThe row of a player will show his/hers result, the columns will show who the match was played against")
        print("\tThe sum of the points will be shown in the total score column for each player."
              "Win = 1 point, draw = 1/2 point, loose = 0 points")
        print("\t* is games not yet played, x is games that wont be played")
        print(division_rows)
        print("|", " "*(col_length + 2), end="") #Leave empty header slot in top-left (position[0][0])

        for player in self.list_players:
            print("|", player.name, " "*(col_length - len(player.name)), end="")
        print("|","Tot score"," "*(col_length - len("Tot score ")),"|",end="\n")
        print(division_rows)

        #Rows
        for player, result_row in enumerate(self.results):
            # Print player name of the winner in the left column
            print("|", (self.list_players[player]).name, " "*(col_length - len((self.list_players[player]).name)), end=" ")

            #Now unwrap the results for that player and print as entries to the same row as the name
            for entry in result_row:
                print("| ", entry, " "*(col_length-len(entry) - 1), end="")
            print("|  ", self.list_players[player].wins, " "*(col_length-len(str(self.list_players[player].wins))-2), end="|\n")
        print(division_rows)

    #Uptades table after one match with param winner and loser player-object
    # @param is_draw is boolean that checks if the game was a draw between the two players, both the "winner"
    # and "loser" then get the same point
    # Winner is rewarded with 1 point on its row
    # Loser get 0 on the row with is name
    def updateTable(self,  winner, loser, is_draw):
        winner_inx = self.list_players.index(winner)
        loser_inx=self.list_players.index(loser)
        if is_draw:
            self.results[winner_inx][loser_inx] = "1/2"
            self.results[loser_inx][winner_inx] = "1/2"
        else:
            self.results[winner_inx][loser_inx] = "1"
            self.results[loser_inx][winner_inx] = "0"





