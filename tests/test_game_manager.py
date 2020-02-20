import sys
sys.path.insert(0, r"C:\UU\VT20\SEPM\updated")
import unittest
from projectse.game_manager import GameManager as GM

class TestGameManager(unittest.TestCase):

    def test_game_manager_string_naive(self):
        """
        Testing if the game_manager can connect to the 
        """
        gm = GM()
        message = "1,2 1,3"
        gm.send(message)
        self.assertEquals(gm.recv(dtype="string"), message)
        gm.close()

if __name__ == '__main__':
    unittest.main()
