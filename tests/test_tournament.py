from projectse.tournament import Tournament
from projectse.round import Round, Match
from projectse.player import *
from unittest.mock import MagicMock
import unittest


class TournamentTestCase(unittest.TestCase):
    def test_ai_play(self):

        t = Tournament(MagicMock())
        #Create AI players
        ai1 = MagicMock()
        ai1.difficuly = AIDifficulty.hi
        ai2 = MagicMock()
        ai2.difficuly = AIDifficulty.low

        #TODO: Rewrite aiplay unittest
        players = [ai1,ai2]
        ai_winner = t.aiplay(ai1, ai2) #Returns an AI player
        self.assertIn(ai_winner, players)

if __name__ == '__main__':
    unittest.main()
