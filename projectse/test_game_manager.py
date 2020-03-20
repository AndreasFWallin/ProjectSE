import sys

sys.path.insert(0, r"C:\UU\VT20\SEPM\updated\ProjectSE")

import unittest
from game_manager import GameManager as GM

class TestGameManager(unittest.TestCase):


    def test_game_manager_json_naive(self):
        """
        Testing if the game_manager can connect to the server and send and recieve a json message
        """
        gm = GM()
        gm.connect()
        gm.send_json()
        recv_msg = gm.recv_json(dtype="json")
        recv_msg = gm.decode(recv_msg)
        self.assertEqual(recv_msg["Difficulty"],2 )
        gm.close()

    def test_game_manager_json_server(self):
        """
        Testing if the game_manager can connect to the server and the server can change the
        """
        gm = GM()
        gm.connect()
        message_board = [-1]*24
        gm.send_json(message_board)
        recv_msg = gm.recv_json(dtype="json")
        recv_msg = gm.decode(recv_msg)
        # message_board[0] = 2
        print(recv_msg)
        self.assertNotEqual(recv_msg["Board"], message_board)
        gm.close()


if __name__ == '__main__':
    unittest.main()
