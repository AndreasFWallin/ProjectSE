import socket
import json


""" Proxy module which handles the communication between Game Engine and Game Platform modules """
class GameManager:
    def __init__(self, ip_adress='130.242.97.115', port=3005):
        """
        Sets up the connection, if the creation of the game manager doesn't work
        make sure you are on the same network, have the same ip and port on server and manager
        """
        self.socket = socket.socket()           # Allocating a socket 
        self.socket.connect((ip_adress, port))  # Connecting the socket to a server, given an ip and port
        print("Connection to server established")

    def send(self, message):
        """
        A function for turning a message into bytes and then send it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').
        """ 
        message_b = bytes(message, 'utf-8')            # Convert the message to bytes
        print(message_b)
        self.socket.send(message_b)           # Send the game state/move
        print("Message sent!")
        
    def recv(self, dtype = "list"):
        """
        A function for recieving a message and turning it from bytes to 
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


    def send_json(self, board = [0]*24,  diff = 1, index_map = None, turn = 0, visual = None):
        """
        A function for turning a message into bytes and then sending it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').
        """ 
        message = {"board":board, "diff":diff, "index_map":index_map, "turn":0, "visual":visual}
        message_json = json.dumps(message)
        message_json_b = bytes(message_json, 'utf-8')            # Convert the message to bytes
        print(message_json_b)
        self.socket.send(message_json_b)           # Send the game state/move
        print("Message sent!")
    

    def recv_json(self, dtype = "json"):
        """
        A function for recieving a message 
        """
        message_recieved = self.socket.recv(1024)
        if dtype == "json":
            message_recieved = json.loads(message_recieved) 
        else:
            print("Warning, incorrect option")
            exit(0)
        print("message_recieved", message_recieved)
        return message_recieved


    def send_json_txt_file(self,  diff = 1, index_map = None, turn = 0, visual = None):
        """
        A function for turning a message into bytes and then sending it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').
        """ 
        with open("../board.txt") as f:
            board = f.readline().split(" ")
        message = {"board":board, "diff":diff, "index_map":index_map, "turn":0, "visual":visual}
        message_json = json.dumps(message)
        message_json_b = bytes(message_json, 'utf-8')            # Convert the message to bytes
        print(message_json_b)
        self.socket.send(message_json_b)           # Send the game state/move
        print("Message sent!")

    def make_move(self, board, turn, difficulty):
        """
        Function to be called when playing a Player vs AI game
        """
        board, difficulty = self.decode(board, difficulty)
        self.send([board, difficulty, turn])
        board, difficulty = self.recv()


    def decode(self, board, difficulty):
        """
        Function for decoding the information that is to be sent to the 
        game engine.
        """
        return board, difficulty

    def close(self):
        """
        Closes the connection
        """
        self.socket.close()
        print("Socket closed")

