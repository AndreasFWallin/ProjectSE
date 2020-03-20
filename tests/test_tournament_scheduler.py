import unittest
from unittest.mock import MagicMock
from projectse.tournament_scheduler import TournamentScheduler

class TournamentSchedulerTestCase(unittest.TestCase):

    def test_get_round(self):
        t1 = TournamentScheduler(3)
        t2 = TournamentScheduler(4)
        t3 = TournamentScheduler(5)
        t4 = TournamentScheduler(6)
        t5 = TournamentScheduler(7)
        t6 = TournamentScheduler(8)

        print("3 player schedule:\n")
        print(t1.get_round(1))
        print(t1.get_round(2))
        print(t1.get_round(3))
        print()
        print("4 player schedule:\n")
        print(t2.get_round(1))
        print(t2.get_round(2))
        print(t2.get_round(3))
        print()
        print("5 player schedule:\n")
        print(t3.get_round(1))
        print(t3.get_round(2))
        print(t3.get_round(3))
        print(t3.get_round(4))
        print(t3.get_round(5))
        print()
        print("6 player schedule:\n")
        print(t4.get_round(1))
        print(t4.get_round(2))
        print(t4.get_round(3))
        print(t4.get_round(4))
        print(t4.get_round(5))
        print()
        print("7 player schedule:\n")
        print(t5.get_round(1))
        print(t5.get_round(2))
        print(t5.get_round(3))
        print(t5.get_round(4))
        print(t5.get_round(5))
        print(t5.get_round(6))
        print(t5.get_round(7))
        print()
        print("8 player schedule:\n")
        print(t6.get_round(1))
        print(t6.get_round(2))
        print(t6.get_round(3))
        print(t6.get_round(4))
        print(t6.get_round(5))
        print(t6.get_round(6))
        print(t6.get_round(7))
        print()
        self.assertEqual(t3.get_round(5),[(4, 2), (5, 1)])

if __name__ == '__main__':
    unittest.main()
