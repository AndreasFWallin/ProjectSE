#from tournament import *
class TournamentDrawer:
    def __init__(self, list_players):
        self.list_players = list_players
        n = len(self.list_players)
        self.results= [[""] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.results[i][j] = "x"


    def drawResultTable(self):
        xwins=33
        #self.updateTable()
        division_rows="|-"+ ("-"*(20+2)+"|")*(len(self.list_players)+2)
        col_length=20

        #Column headers
        print("Tournament Results")
        print(division_rows)
        print("|", " " *(col_length+2), end="")
        for player in self.list_players:
            print("|", player.name, " " *(col_length-len(player.name)), end="")
        print("|","Total score"," " *(col_length-len("Total score ")),"|",end="\n")
        print(division_rows)

        for player, row in enumerate(self.results):
            print("|", (self.list_players[player]).name, " " * (col_length - len((self.list_players[player]).name)), end=" ")

            for entry in row:
                print("| ", entry, " " * (col_length-len(entry)-1), end="")
            print("|  ", self.list_players[player].wins, " " * (col_length-len(str(self.list_players[player].wins))-2), end="|\n")
        print(division_rows)

    #Takes the round played and updates it from the list of winners after the current round.
    #Rounds start at 0,
    def updateTable(self, num_Round, list_winners):
        for i in range(len(self.results)):
            if i in list_winners:
                self.results[i][num_Round]="1"
            elif self.results[num_Round][i] is not 'x':
                self.results[i][num_Round]="0"
        self.drawResultTable()


