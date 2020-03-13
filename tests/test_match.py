import unittest
from projectse.round import Match
from unittest.mock import MagicMock

class MatchTestCase(unittest.TestCase):

  def test_create_match(self):
    player_mock_white = MagicMock()
    player_mock_white.name = "test1"

    player_mock_black = MagicMock()
    player_mock_black.name = "test2"
    match = Match(player_mock_white, player_mock_black) 

    #Get names of the different players
    self.assertEqual("test1", match.get_white_player_name())
    self.assertEqual("test2", match.get_black_player_name())

    #Currently have no winner
    self.assertEqual('Not played!', match.get_winner_name())

    #Set winner to player one
    match.set_winner(player_mock_white)
    self.assertEqual("test1", match.get_winner_name())

    #Set winner to player two
    match.set_winner(player_mock_black)
    self.assertEqual("test2", match.get_winner_name())

if __name__ == '__main__':
  unittest.main()
