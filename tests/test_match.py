import unittest
from projectse.round import Match
from projectse.player import Player
from projectse.configuration import Configuration

class MatchTestCase(unittest.TestCase):

  def test_create_match(self):
    player_one = Player("test1")
    player_two = Player("test2")

    cfg = Configuration()
    cfg.set_players([player_one, player_two])

    player_tuple = (1, 2)

    match = Match(player_tuple, cfg)

    #Get names of the different players
    self.assertEqual("test1", match.get_white_player_name())
    self.assertEqual("test2", match.get_black_player_name())

    #Currently have no winner
    self.assertEqual(None, match.get_winner())

    #Set winner to player one
    match.set_winner(1)
    self.assertEqual("test1", match.get_winner())

    #Set winner to player two
    match.set_winner(2)
    self.assertEqual("test2", match.get_winner())

if __name__ == '__main__':
  unittest.main()
