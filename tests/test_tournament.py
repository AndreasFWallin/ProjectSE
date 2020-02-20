from projectse.tournament import Tournament
from projectse.round import Round, Match
from projectse.player import *
from unittest.mock import MagicMock
import unittest
from itertools import permutations

class TournamentTestCase(unittest.TestCase):


    def test_ai_play(self):
        diff_lookup={AIDifficulty.low:1,AIDifficulty.med:2,AIDifficulty.hi:3}
        t = Tournament(MagicMock())
        #Create AI players

        perm = permutations([AIDifficulty.low, AIDifficulty.hi, AIDifficulty.med], 2)
        player_combinations=[]
        for p1,p2 in perm:
            ai1 = MagicMock()
            ai2 = MagicMock()
            ai1.difficulty = p1
            ai2.difficulty = p2
            player_combinations.append((ai1,ai2))
            player_combinations.append((ai2,ai1))

        num_matches = 100
        uncertainty_interval = 30 #in percent

        #TODO: Rewrite aiplay unittest
        for ai1,ai2 in player_combinations:
            players=[ai1,ai2]
            ai1_win_cnt=0
            ai2_win_cnt=0
            for i in range(num_matches):
                ai_winner = t.aiplay(ai1, ai2) #Returns an AI player
                self.assertIn(ai_winner, players)
                if(ai_winner==ai1):
                    ai1_win_cnt+=1
                else:
                    ai2_win_cnt+=1
        difficulty_diff = diff_lookup[ai1.difficulty]-diff_lookup[ai2.difficulty]
        a1_win_ratio={0:0.5,1:0.35,2:0.15}
        a1_loose_ratio = {0: 0.5, 1: 0.65, 2: 0.85}

        actual_ratio = ai1_win_cnt/num_matches
        #if ai1 is weaker than ai2
        if difficulty_diff < 0:
            prob_diff = actual_ratio-a1_loose_ratio[abs(difficulty_diff)]
        else:
            prob_diff = actual_ratio-a1_win_ratio[difficulty_diff]
        prob_diff=abs(prob_diff)
        #Check that the ratio is close enough to real deal.
        # its random after all.
        self.assertLess(prob_diff, uncertainty_interval/100,str(ai1.difficulty)+"vs"+str(ai2.difficulty))




    def test_tournament(self):

if __name__ == '__main__':
    unittest.main()
