import unittest
from projectse.round import Round, Match
from projectse.player import Player
from projectse.configuration import Configuration

class RoundTestCase(unittest.TestCase):

  def test_create_round(self):
    # Create players
    player_one = Player("test1")
    player_two = Player("test2")
    player_three = Player("test3")
    player_four = Player("test4")

    # Create configuration
    cfg = Configuration()
    cfg.set_players([player_one, player_two, player_three, player_four])

    # Create list of matches
    matches = [(1,2), (3,4)]

    # Create round
    round = Round(matches, cfg)

    # No match is currently being played
    self.assertEqual(None, round.get_current_match())
    # No matches have been played yet
    self.assertEqual([], round.get_played_matches())

    # Set next match to be played
    round.set_next_match()
    # White player of first match is player_one
    self.assertEqual("test1", round.get_current_match().get_white_player_name())
    # Current match is only matched played so far
    self.assertEqual([], round.get_played_matches())

    round.set_next_match()
    played_match = round.get_played_matches()[0]
    self.assertEqual("test1", played_match.get_white_player_name())
    self.assertEqual("test2", played_match.get_black_player_name())

    current_match = round.get_current_match()
    self.assertEqual("test3", current_match.get_white_player_name())
    self.assertEqual("test4", current_match.get_black_player_name())

    self.assertEqual([], round.get_unplayed_matches())

if __name__ == '__main__':
  unittest.main()
