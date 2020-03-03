import unittest
from projectse.tournament_drawer import *
from projectse.player import *

class TournamentDrawerTestCase(unittest.TestCase):

    def test_drawer(self):
        player_list = []
        player_list.append(Player("A"))
        player_list.append(Player("B"))
        player_list.append(Player("C"))
        player_list.append(Player("D"))

        td = TournamentDrawer()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
