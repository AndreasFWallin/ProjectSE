import unittest
from unittest.mock import MagicMock
from projectse.tournament_scheduler import TournamentScheduler

class TournamentSchedulerTestCase(unittest.TestCase):

    def test_get_round(self):
        t1 = TournamentScheduler(3)
        t2 = TournamentScheduler(4)
        t3 = TournamentScheduler(8)

        print("3 players, Round 3:\n")
        print(t1.get_round(3))
        print()
        #self.assertEqual(t1.get_round(3),[(3,1)])
        print("4 players, Round 2:\n")
        print(t2.get_round(2))
        print()
        #self.assertEqual(t2.get_round(2),[(4,1),(2,3)])
        print("8 players, Round 6:\n")
        print(t3.get_round(6))
        print()
        #self.assertEqual(t3.get_round(6),[(3,2),(5,8),(7,6),(1,4)])

if __name__ == '__main__':
    unittest.main()
