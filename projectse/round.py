
class Round:
    """ A Gameround with responsibility for keeping track of the status of
    a single game round  """
    def __init__(self, ):
        self.matches = []
        self.current_match_inx = 0

    def add_match(self, match):
        self.matches.append(match)

    def get_matches(self):
        return self.matches

    def get_current_match(self):
        if len(self.matches) == 0:
            return None
        return self.matches[self.current_match_inx]

    def get_next_match(self):
        #-1 since 0-indexed
        if self.current_match_inx < len(self.matches)-1:
            self.current_match_inx+=1
            return self.get_current_match()
        else:
            return None

    def get_played_matches(self):
        played_matches = filter(lambda x: x.is_played(), self.matches)
        return played_matches

    def get_unplayed_matches(self):
        unplayed_matches = filter(lambda x: not x.is_played(), self.matches)
        return unplayed_matches


class Match:
    """ A Match responsible for keeping track of the result of a single match """
    def __init__(self, white, black):
        self.white_player = white
        self.black_player = black
        self.winner = None
        self.played = False

    def only_ai(self):
        return self.black_player.is_ai() and self.white_player.is_ai()

    def print_playing(self):
        print("Now playing, ", self.get_white_player_name(),
              " as white, versus ", self.get_black_player_name(),
              "as black")
        print()

    def get_winner_name(self):
        if self.played:
            if self.winner is not None:
                return self.winner.name
            else:
                return "No one"
        return "Not played!"

    def is_played(self):
        return self.played


    def set_winner(self, player):
        self.played = True
        self.winner = player

    def get_white_player(self):
        return self.white_player

    def get_black_player(self):
        return self.black_player

    def get_white_player_name(self):
        return self.white_player.name

    def get_black_player_name(self):
        return self.black_player.name

  
  