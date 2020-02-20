import sys
<<<<<<< HEAD
sys.path.insert(0, r"C:\UU\VT20\SEPM\updated\ProjectSE")
=======
sys.path.insert(0, r"C:\UU\VT20\SEPM\updated")
>>>>>>> fd31481487725b337dbe058af168a5af20bdfa97
import unittest
from projectse.game_manager import GameManager as GM

class TestGameManager(unittest.TestCase):

    def test_game_manager_string_naive(self):
        """
        Testing if the game_manager can connect to the server
        """
        gm = GM()
        message = "1,2 1,3"
        gm.send(message)
        recv_msg =  gm.recv(dtype="string")
        self.assertEqual(recv_msg, message)
        gm.close()
    def test_game_manager_json_naive(self):
        """
        Testing if the game_manager can connect to the server and send and recieve a json message
        """
        gm = GM()
        gm.send_json()
        recv_msg = gm.recv_json(dtype="json")
        self.assertEqual(recv_msg["diff"], 1)
        gm.close()

    def test_game_manager_json_server(self):
        """
        Testing if the game_manager can connect to the server and the server can change the 
        """
        gm = GM()
        message_board = [1]*24
        gm.send_json(message_board)
        recv_msg = gm.recv_json(dtype="json")
        message_board[0] = 2
        self.assertEqual(recv_msg["board"], message_board)
        gm.close()

    def test_game_manager_json_txt_naive(self):
        """
        Testing if the game_manager can connect to the 
        """
        gm = GM()
        gm.send_json_txt_file()
        recv_msg =  gm.recv_json(dtype="json")
        self.assertEqual(recv_msg["diff"], 1)
        gm.close()

if __name__ == '__main__':
    unittest.main()
