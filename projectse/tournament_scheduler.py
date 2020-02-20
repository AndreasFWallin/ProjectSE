class TournamentScheduler:
    def __init__(self, players):
        self.num_players = players
        self.schedule = []

        """ Creating a tournament schedule consisting of an array (schedule)
            containing arrays with tuples, representing matches. """
        teams = []
        for i in range(1,players+1):
            teams.append(i)

        if (players % 2) == 1:
            teams.append(0)
            for round in range(1,players):
                matches = []
                for i in range(len(teams) / 2):
                    if (teams[i] != 0) and (teams[len(teams) - i - 1] != 0):
                        if (round % 2) == 0:
                            matches.append((teams[i], teams[len(teams) - i - 1]))
                            teams.insert(1, teams.pop())
                            schedule.append(matches)
                        else:
                            matches.append((teams[len(teams) - i - 1], teams[i]))
                            teams.insert(1, teams.pop())
                            schedule.append(matches)

        else:
            for round in range(players - 1):
                matches = ()
                for i in range(len(teams) / 2):
                    if (round % 2) == 0:
                        matches.append((teams[i], teams[len(teams) - i - 1]))
                        teams.insert(1, teams.pop())
                        schedule.append(matches)
                    else:
                        matches.append((teams[len(teams) - i - 1], teams[i]))
                        teams.insert(1, teams.pop())
                        schedule.append(matches)


    """ get_round takes an integer (1-7) as an input and returns
        an array with a description of a round. On the form
        of tuples representing the games"""
    def get_round(self, round_num):
        return self.schedule[round_num-1]
