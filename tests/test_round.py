import unittest
from projectse.round import Round
from unittest.mock import MagicMock

class RoundTestCase(unittest.TestCase):

  def test_create_round(self):
    player_mock_white_1 = MagicMock()
    player_mock_white_1.get_name.return_value = "Hej"
    player_mock_white_1.name = "test1"

    player_mock_black_1 = MagicMock()
    player_mock_black_1.get_name.return_value = "Hej"
    player_mock_black_1.name = "test2"

    player_mock_white_2 = MagicMock()
    player_mock_white_2.get_name.return_value = "Hej"
    player_mock_white_2.name = "test3"

    player_mock_black_2 = MagicMock()
    player_mock_black_2.get_name.return_value = "Hej"
    player_mock_black_2.name = "test4"

    match1 = MagicMock()
    match1.white_player = player_mock_white_1
    match1.get_white_player_name.return_value = player_mock_white_1.name
    match1.get_black_player_name.return_value = player_mock_black_1.name
    match1.black_player = player_mock_black_1
    
    match2 = MagicMock()
    match2.white_player = player_mock_white_2
    match2.get_white_player_name.return_value = player_mock_white_2.name
    match2.get_black_player_name.return_value = player_mock_black_2.name
    match2.black_player = player_mock_black_2

    # Create round
    round = Round()
    self.assertEqual(None, round.get_current_match())
    # Add first match 
    round.add_match(match1)
    # Assert there is only one match in the round
    self.assertEqual(1, len(round.get_matches()))
    # Assert no match is currently being played
    self.assertEqual(match1, round.get_current_match())
    # White player of first match is player_mock_white_1
    self.assertEqual("test1", round.get_current_match().get_white_player_name())
    # White player of first match is player_mock_black_1
    self.assertEqual("test2", round.get_current_match().get_black_player_name())

    # Add new match
    round.add_match(match2)
    # Assert there are two matches in the round
    self.assertEqual(2, len(round.get_matches()))
    # Set next match to be played
    round.get_next_match()
    # White player of first match is player_mock_white_2
    self.assertEqual("test3", round.get_current_match().get_white_player_name())
    # White player of first match is player_mock_black_2
    self.assertEqual("test4", round.get_current_match().get_black_player_name())



if __name__ == '__main__':
  unittest.main()
