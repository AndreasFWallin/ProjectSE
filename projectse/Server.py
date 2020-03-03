# Import socket module 
import socket
import json   
import GameEngine12             

class Server():
    def __init__(self, address, port=3005):
        # Create a socket object 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        
        # connect to the server on local computer 
        self.s.bind((address, port))

    def accept(self):
        """
        Here the server accepts a new request
        """
        self.s.listen(5)
        self.c, self.addr = self.s.accept()

    def recv(self):
        """
        Here the game engine waits for a message from the platform
        :return: message, a json object 
        """
        print("Move recieved")
        message = self.c.recv(1024)
        return message

    def send(self, message):
        """
        Here the game engine sends a response
        param: message, a json message
        """
        self.c.send(message)
        print("Move sent")
    
    def close(self):
        self.c.close()

    def is_json(self, myjson):
        """
        checking to see if a file is a json
        """
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True


if __name__ == "__main__":
    serv = Server('192.168.0.101')
    msg = None
    while (True):
        serv.accept()
        msg = serv.recv()
        with open('board.json', 'w', encoding='utf-8') as f:
            json.dump(msg, f)
        GameEngine12.runUUGame('board.json')
        with open ('board.json', 'r', encoding='utf-8') as f:
            msg = json.load(f)
        serv.send(msg)
    serv.close()



