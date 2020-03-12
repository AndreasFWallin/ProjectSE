import sys
import time
sys.path.insert(0, r"C:\UU\VT20\SEPM\updated\ProjectSE")

import unittest
from projectse.game_manager import GameManager as GM

class TestGameManager(unittest.TestCase):


    def test_game_manager_json_naive(self):
        """
        Testing if the game_manager can connect to the server and send and recieve a json message
        """
        print("please")
        gm = GM()
        gm.connect('192.168.0.105')
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
        gm.connect('192.168.0.105')
        message_board = [-1]*24
        gm.send_json(message_board)
        recv_msg = gm.recv_json(dtype="json")
        recv_msg = gm.decode(recv_msg)
        # message_board[0] = 2
        print(recv_msg)
        self.assertNotEqual(recv_msg["Board"], message_board)
        gm.close()

    def test_game_manager_make_first_move(self):
        """
        Testing if the game_manager can connect to the server and the server can change the 
        """
        gm = GM()
        gm.connect('192.168.0.105')
        message_board = [-1]*24
        gm.make_move(message_board, turn=0, player=0, difficulty=3)
        recv_msg = gm.recv_json(dtype="json")
        recv_msg = gm.decode(recv_msg)
        # message_board[0] = 2
        print(recv_msg)
        self.assertNotEqual(recv_msg["Board"], message_board)
        gm.close()

    def test_game_manager_AI_self_play_high_low(self):
        """
        Testing if the game_manager can connect to the server and the server can change the 
        """
        gm = GM()
        gm.connect('192.168.0.105')
        message_board = [-1]*24
        turn = 0
        while True:
            old_board = message_board
            message_board = gm.make_move(message_board, turn=0, player=0, difficulty=3)
            print(message_board)
            message_board = gm.make_move(message_board, turn=0, player=1, difficulty=1)
            turn += 1
            print(message_board)
            time.sleep(0.2)
            if old_board == message_board:
                break
        gm.close()   

    

    
if __name__ == '__main__':
    unittest.main()
