""" Creating a tournament schedule consisting of an array (schedule)
    containing arrays with tuples, representing matches. """
class TournamentScheduler:
    def __init__(self, players):
        self.num_players = players
        self.schedule = []

        if (players == 3):
            self.schedule.append([(2,3)])
            self.schedule.append([(1, 2)])
            self.schedule.append([(3, 1)])
        elif (players == 4):
            self.schedule.append([(1, 4), (2, 3)])
            self.schedule.append([(4, 3), (1, 2)])
            self.schedule.append([(2, 4), (3, 1)])
        elif (players == 5):
            self.schedule.append([(2, 5), (3, 4)])
            self.schedule.append([(5, 3), (1, 2)])
            self.schedule.append([(3, 1), (4, 5)])
            self.schedule.append([(1, 4), (2, 3)])
            self.schedule.append([(4, 2), (5, 1)])
        elif (players == 6):
            self.schedule.append([(1, 6), (2, 5), (3, 4)])
            self.schedule.append([(6, 4), (5, 3), (1, 2)])
            self.schedule.append([(2, 6), (3, 1), (4, 5)])
            self.schedule.append([(6, 5), (1, 4), (2, 3)])
            self.schedule.append([(3, 6), (4, 2), (5, 1)])
        elif (players == 7):
            self.schedule.append([(2, 7), (3, 6), (4, 5)])
            self.schedule.append([(6, 4), (7, 3), (1, 2)])
            self.schedule.append([(3, 8), (4, 7), (5, 6)])
            self.schedule.append([(7, 5), (1, 4), (2, 3)])
            self.schedule.append([(4, 2), (5, 1), (6, 7)])
            self.schedule.append([(1, 6), (2, 5), (3, 4)])
            self.schedule.append([(5, 3), (6, 2), (7, 1)])
        elif (players == 8):
            self.schedule.append([(1, 8), (2, 7), (3, 6), (4, 5)])
            self.schedule.append([(8, 5), (6, 4), (7, 3), (1, 2)])
            self.schedule.append([(2, 8), (3, 1), (4, 7), (5, 6)])
            self.schedule.append([(8, 6), (7, 5), (1, 4), (2, 3)])
            self.schedule.append([(3, 8), (4, 2), (5, 1), (6, 7)])
            self.schedule.append([(8, 7), (1, 6), (2, 5), (3, 4)])
            self.schedule.append([(4, 8), (5, 3), (6, 2), (7, 1)])


    """ get_round takes an integer (1-7) as an input and returns
        an array with a description of a round. On the form
        of tuples representing the games"""
    def get_round(self, round_num):
        return self.schedule[round_num-1]
