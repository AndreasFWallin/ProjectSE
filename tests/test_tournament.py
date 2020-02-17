from projectse.tournament import Tournament
from projectse.round import Round, Match
from projectse.player import Player, AIPlayer
import unittest


class TournamentTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    
        #Create AI players
        ai1 = AIPlayer("test 1","lo")
        ai2 = AIPlayer("test 2","lo")
        ai3 = AIPlayer("test 3","mid")
        ai4 = AIPlayer("test 4","hi")
        #TODO: Rewrite aiplay unittest
        #aiplay() Returns an AI player
        self.assertIsInstance(aiplay(ai1,ai2),AIPlayer)

if __name__ == '__main__':
    unittest.main()
