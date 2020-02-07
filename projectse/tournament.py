class Round:
    """ A Gameround with responsibility for keeping track of the status of a single game round  """
    pass

class Tournament:
    """ Tournament is responsible for handling a round-robin tournament for a two player game based on a collection of
        players (which players and their properties is decided elsewhere). It keeps track of current game, next game, who won etc. """
    def start_tournament(self):
        pass

    def stop_tournament(self):
        pass
