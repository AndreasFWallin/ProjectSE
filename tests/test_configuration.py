import unittest
from unittest.mock import MagicMock
from projectse.configuration import ConfigurationBuilder

class ConfigurationBuilderTestCase(unittest.TestCase):

    def test_set_players(self):

        cb = ConfigurationBuilder(MagicMock())
        cb.get_number_input = MagicMock()
        # Set number of total and Ai players
        cb.get_number_input.side_effect = [8, 3]

        cb.get_char_input = MagicMock()
        # Sets difficulty to AI players
        cb.get_char_input.side_effect = ["H", "M", "L"]

        cb.get_input = MagicMock()
        # Sets names of AI players
        cb.get_input.side_effect = ["Kalle", "Emma", "Kim", "Olle","Ken"]
        cb.configure_players = MagicMock()
        cb.query_players()
        arg, kwargs = cb.configure_players.call_args
        players_list = arg[0]
        player_names = ["AIPlayer1", "AIPlayer2", "AIPlayer3", "Kalle", "Emma", "Kim", "Olle","Ken"]
        for player,name in zip(players_list, player_names):
            print(str(player)+" name:"+str(name))
            self.assertEqual(player.name,name)

if __name__ == '__main__':
    unittest.main()
