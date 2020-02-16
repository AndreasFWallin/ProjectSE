class Round:
  """ A Gameround with responsibility for keeping track of the status of a single game round  """
  def __init__(self, matches, configuration):
    self.matches = matches
    self.cfg = configuration
    self.unplayed_matches = []
    self.played_matches = []
    self.current_match = None

    for i in range(len(matches)):
      self.unplayed_matches.append(Match(self.matches[i], self.cfg))

  def get_current_match(self):
    return self.current_match

  def get_played_matches(self):
    return self.played_matches

  def get_unplayed_matches(self):
    return self.unplayed_matches

  def set_next_match(self):
    if self.unplayed_matches != []:
      if self.current_match != None:
        self.played_matches.append(self.current_match)
        
      self.current_match = self.unplayed_matches.pop(0)

  def set_winner(self, player):
    if self.current_match != None:
      self.current_match.set_winner(player)
    else:
      return
    

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
  
  
  def aiplay(player1,player2):
    if(isinstance(player1,AIPlayer) and isinstance(player2,AIPlayer)):
        if(player1.difficulty=="lo" and player2.difficulty=="lo"):
            if(randrange(100)<50):
                player1.result=True
                player2.result=False;
            else:
                player2.result=True
                player1.result=False;
        
        elif(player1.difficulty=="lo" and player2.difficulty=="mid"):
            if(randrange(100)<35):
                player1.result=True
                player2.result=False
            else:
                player1.result=False
                player2.result=True;
        elif(player1.difficulty=="lo"and player2.difficulty=="hi"):
            if(randrange(100)<15):
                player1.result=True
                player2.result=False
            else:
                player1.result=False
                player2.result=True;
        elif(player1.difficulty=="mid"and player2.difficulty=="lo"):
            if(randrange(100)<35):
                player1.result=False
                player2.result=True
            else:
                player1.result=True
                player2.result=False;
        elif(player1.difficulty=="mid"and player2.difficulty=="mid"):
            if(randrange(100)<50):
                player1.result=True
                player2.result=False
            else:
                player1.result=False
                player2.result=True;
        elif(player1.difficulty=="mid"and player2.difficulty=="hi"):
            if(randrange(100)<35):
                player1.result=True
                player2.result=False
            else:
                player1.result=False
                player2.result=True;
        elif(player1.difficulty=="lo"and player2.difficulty=="mid"):
            if(randrange(100)<35):
                player1.result=True
                player2.result=False
            else:
                player1.result=False
                player2.result=True;
        elif(player1.difficulty=="hi"and player2.difficulty=="lo"):
            if(randrange(100)<15):
                player1.result=False
                player2.result=True
            else:
                player1.result=True
                player2.result=False;
        elif(player1.difficulty=="hi"and player2.difficulty=="mid"):
            if(randrange(100)<35):
                player1.result=False
                player2.result=True
            else:
                player1.result=True
                player2.result=False;
        elif(player1.difficulty=="hi"and player2.difficulty=="hi"):
            if(randrange(100)<50):
                player1.result=True
                player2.result=False
            else:
                player1.result=False
                player2.result=True;
                
