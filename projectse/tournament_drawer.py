#from tournament import *
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
        col_length = 12
        division_rows="|-"+ ("-"*(col_length+2)+"|")*(len(self.list_players)+2)


        #Column headers
        print("Tournament Results")
        print(division_rows)
        print("|", " " *(col_length+2), end="")
        for player in self.list_players:
            print("|", player.name, " " *(col_length-len(player.name)), end="")
        print("|","Total score"," " *(col_length-len("Total score ")),"|",end="\n")
        print(division_rows)

        #Rows
        for player, row in enumerate(self.results):
            print("|", (self.list_players[player]).name, " " * (col_length - len((self.list_players[player]).name)), end=" ")

            for entry in row:
                print("| ", entry, " " * (col_length-len(entry)-1), end="")
            print("|  ", self.list_players[player].wins, " " * (col_length-len(str(self.list_players[player].wins))-2), end="|\n")
        print(division_rows)

    #Uptades table after one match with param winner and loser player-object
    # Winner is rewarded with 1 point on its row
    # Loser get 0 on the row with is name
    def updateTable(self,  winner, loser):
        winner_inx = self.list_players.index(winner)
        loser_inx=self.list_players.index(loser)
        self.results[winner_inx][loser_inx] = "1"
        self.results[loser_inx][winner_inx] = "0"





