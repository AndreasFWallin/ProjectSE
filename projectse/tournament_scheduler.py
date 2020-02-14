class TournamentScheduler:
    def __init__(self, players):
        self.num_players=players


    """ get_round takes an integer (1-7) as an input and returns
        an array with a description of a round. On the form
        of tuples representing the games"""
    def get_round(self, round_num):
        if (self.num_players == 3):
            if (round_num == 1):
                return [(1,2)]
            elif (round_num == 2):
                return [(2,3)]
            elif (round_num == 3):
                return [(3,1)]
            else:
                pass

        elif(self.num_players == 4):
            if (round_num == 1):
                return [(1,3),(4,2)]
            elif (round_num == 2):
                return [(4,1),(2,3)]
            elif (round_num == 3):
                return [(1,2),(3,4)]
            else:
                pass

        elif(self.num_players == 5):
            if (round_num == 1):
                return [(4,3),(5,2)]
            elif (round_num == 2):
                return [(3,5),(1,4)]
            elif (round_num == 3):
                return [(2,4),(3,1)]
            elif (round_num == 4):
                return [(5,1),(2,3)]
            elif (round_num == 5):
                return [(1,2),(4,5)]
            else:
                pass

        elif(self.num_players == 6):
            if (round_num == 1):
                return [(5,3),(1,6),(2,4)]
            elif (round_num == 2):
                return [(4,1),(2,5),(6,3)]
            elif (round_num == 3):
                return [(2,6),(3,1),(4,5)]
            elif (round_num == 4):
                return [(1,5),(6,4),(3,2)]
            elif (round_num == 5):
                return[(3,4),(1,2),(5,6)]
            else:
                pass

        elif(self.num_players == 7):
            if (round_num == 1):
                return [(1,3),(2,7),(4,6)]
            elif (round_num == 2):
                return [(4,7),(6,3),(2,5)]
            elif (round_num == 3):
                return [(6,1),(5,4),(7,3)]
            elif (round_num == 4):
                return [(3,2),(7,6),(5,1)]
            elif (round_num == 5):
                return [(7,5),(4,1),(6,2)]
            elif (round_num == 6):
                return [(2,4),(3,5),(1,7)]
            elif (round_num == 7):
                return [(5,6),(1,2),(3,4)]
            else:
                pass

        elif(self.num_players == 8):
            if (round_num == 1):
                return [(4,7),(6,3),(8,1),(2,5)]
            elif (round_num == 2):
                return [(6,1),(4,5),(2,7),(8,3)]
            elif (round_num == 3):
                return [(2,8),(7,1),(5,3),(4,6)]
            elif (round_num == 4):
                return [(1,3),(2,4),(6,8),(5,7)]
            elif (round_num == 5):
                return [(8,4),(3,7),(1,5),(6,2)]
            elif (round_num == 6):
                return [(3,2),(5,8),(7,6),(1,4)]
            elif (round_num == 7):
                return [(5,6),(1,2),(3,4),(7,8)]
            else:
                pass
