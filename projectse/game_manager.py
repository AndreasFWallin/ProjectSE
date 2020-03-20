import socket
import json
from projectse.configuration import *

class BoardState:
    def __init__(self):
        self.finished = False
        self.is_draw = False
        self.turn = 0
        self.difficulty = 0

        self.index_map = {
            "A": " 0------- 1------- 2",
            "B": " |        |        |",
            "C": " |  8---- 9----10  |",
            "D": " |  |     |     |  |",
            "E": " |  | 16-17-18  |  |",
            "F": " |  | |      |  |  |",
            "G": " 7-15-23    19-11- 3",
            "H": " |  | |      |  |  |",
            "I": " |  | 22-21-20  |  |",
            "J": " |  |     |     |  |",
            "K": " | 14----13----12  |",
            "L": " |        |        |",
            "M": " 6------- 5------- 4"
        }

        self.visual = {
            "A": " ----- ----- ",
            "B": "|     |     |",
            "C": "|  --- ---  |",
            "D": "| |   |   | |",
            "E": "| |  - -  | |",
            "F": "| | |   | | |",
            "G": " - -     - - ",
            "H": "| | |   | | |",
            "I": "| |  - -  | |",
            "J": "| |   |   | |",
            "K": "|  --- ---  |",
            "L": "|     |     |",
            "M": " ----- ----- "
        }

        self.player = 0
        self.turn = 0
        self.board = {}
        for i in range(24):
            self.board.update({str(i): -1})

    def is_finished(self):
        return self.finished

    def get_player_color(self):
        if self.turn % 2 == 0:
            return "Black"
        else:
            return "White"

    def set_difficulty(self, difficulty):
        this.difficulty = difficulty

    def set_finished(self):
        self.finished = True

    def set_draw(self):
        self.is_draw = True

""" Proxy module which handles the communication between Game Engine and Game Platform modules """


class GameManager:

    def __init__(self):
        """
        Sets up the connection, if the creation of the game manager doesn't work
        make sure you are on the same networ, have the same ip and port on server and manager
        """
        print("init")
        self.socket = socket.socket()           # Allocating a socket

    def connect(self,ip_adress='192.168.0.101', port=3000):
        self.socket.connect((ip_adress, port))  # Connecting the socket to a server, given an ip and port
        print("Connection to server established")

    def send(self, message, dtype="list"):
        """
        A function for turning a message into bytes and then send it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').
        """
        if dtype == "list":
            message_b = bytes(message)            # Convert the message to bytes
        if dtype == "string":
            message_b = bytes(message, 'utf-8')
        print(message_b)
        self.socket.send(message_b)           # Send the game state/move
        print("Message sent!")

    def recv(self, dtype = "list"):
        """
        A function for recieving a message and   turning it from bytes to
        list or string, depending on the input
        """
        message_recieved = self.socket.recv(1024)
        if dtype == "list":
            message_recieved = list(message_recieved)
        # TODO add the necessary transformation of the data
        elif dtype == "string":
            message_recieved = message_recieved.decode()
        else:
            print("Warning, incorrect option")
            exit(0)
        print("message_recieved", message_recieved)
        return message_recieved


    def send_json(self, board = [-1]*24,  diff = 2, index_map = None, turn = 1, visual = None, player=1):
        """
        A function for turning a message into bytes and then sending it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').
        """
        board[11] = 0
        message = {"Board":board, "Difficulty":diff, "Index Map":index_map,
                 "Turn":turn, "Visual":visual, "Player":player}
        message_json = json.dumps(message)
        message_json_b = bytes(message_json, 'utf-8')            # Convert the message to bytes
        print(message_json_b)
        self.socket.send(message_json_b)           # Send the game state/move
        print("Message sent!")


    def recv_json(self, dtype = "json"):
        """
        A function for recieving a message
        """
        print("recv init")
        message_recieved = self.socket.recv(1024)
        print("recieved")
        if dtype == "json":
            msg = json.loads(message_recieved.decode('utf-8'))
        else:
            print("Warning, incorrect option")
            exit(0)
        print("message_recieved", message_recieved)
        return message_recieved

    """
    def send_json_txt_file(self,  diff = 1, index_map = None, turn = 0, visual = None):

        A function for turning a message into bytes and then sending it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').

        with open("board.json") as f:
            board = f.readline().split(" ")
        message = {"Board":board, "Difficulty":diff, "Index_map":index_map, "Turn":0, "Visual":visual}
        message_json = json.dumps(message)
        message_json_b = bytes(message_json, 'utf-8')            # Convert the message to bytes
        print(message_json_b)
        self.socket.send(message_json_b)           # Send the game state/move
        print("Message sent!")
    """

    def make_move_more_data(self, board, turn, difficulty, player):
        """
        Function to be called when playing a Player vs AI game
        """
       # board, difficulty = self.decode({"Board":board, "Difficulty":difficulty})
        self.send_json(board=board, turn=turn, diff=difficulty, player=player)
        msg = self.recv_json()
        msg = self.decode(msg)
        board = msg["Board"]
        turn = msg["Turn"]
        difficulty = msg["Difficulty"]
        player = msg["Player"]
        return board, turn, difficulty, player

    def make_move_test(self, board, player, turn, difficulty):
        """
        Function to be called when playing a Player vs AI game
        """
        print("move initiated")
        self.send_json(board, difficulty, turn=turn, player=player)
        message = self.recv_json()
        message = self.decode(message)
        board_raw = message["Board"]
        board_tuples = board_raw.items()
        board = [position[1] for position in board_tuples]
        print(message["Visual"])
        return board

    def make_move(self, board):
        """
        Function to be called when playing a Player vs AI game
        """
        print("move initiated")
        self.send_json(board, difficulty, turn=board.turn, player=player)
        message = self.recv_json()
        message = self.decode(message)
        board_raw = message["Board"]
        board_tuples = board_raw.items()
        board = [position[1] for position in board_tuples]
        print(message["Visual"])
        return board



    def decode(self, byte_msg):
        """
        Function for decoding the information that is to be sent to the
        game engine.
        """
        decoded_msg = json.loads(byte_msg.decode('utf-8'))
        return decoded_msg

    def close(self):
        """
        Closes the connection
        """
        self.socket.close()
        print("Socket closed")
