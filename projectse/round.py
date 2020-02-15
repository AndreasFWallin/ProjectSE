class Round:
  """ A Gameround with responsibility for keeping track of the status of a single game round  """
  def __init__(self, configuration):
    pass

class Match:
  """ A Match responsible for keeping track of the result of a single match """
  def __init__(self, players, configuration):
    self.cfg = configuration
    self.white_player = self.cfg.players[players[0] - 1]
    self.black_player = self.cfg.players[players[1] - 1]
    self.winner = None

  def get_winner(self):
    return self.winner

  def set_winner(self, player):
    self.winner = self.cfg.players[player - 1].name

  def get_white_player(self):
    return self.white_player

  def get_black_player(self):
    return self.black_player  

  def get_white_player_name(self):
    return self.white_player.name

  def get_black_player_name(self):
    return self.black_player.name
