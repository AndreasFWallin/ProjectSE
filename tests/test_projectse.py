import unittest
from unittest.mock import MagicMock,call
from project_se import ProjectSE

class ProjectSETestCase(unittest.TestCase):

    def test_tournament_play(self):
        tournament = MagicMock()
        match = MagicMock()
        match2 = MagicMock()
        match3 = MagicMock()
        matches = [match,match2,match3]

        for m in matches:
            m.only_ai.return_value = False

        tournament = MagicMock()
        round = MagicMock()
        round2 = MagicMock()

        tournament.get_current_round.return_value = round
        tournament.get_current_match.side_effect = [match, match3]
        tournament.get_next_match.side_effect = [match2, None, None]
        tournament.get_next_round.side_effect = [round2, None]

        proj = ProjectSE()
        proj.play_match = MagicMock()
        proj.play_tournament(tournament)

        proj.play_match.assert_has_calls([call(match),call(match2),call(match3)],any_order=False)


if __name__ == '__main__':
    unittest.main()
