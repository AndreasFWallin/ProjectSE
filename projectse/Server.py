# Import socket module 
import socket
import json                

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
        serv.send(msg)
    serv.close()


"""
    # Create a socket object 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    
    # connect to the server on local computer 
    s.bind(('192.168.0.101', port))

    while True:
        c, addr = s.accept()
        print("Connection established!")
        message = c.recv(1024)
        if False: # is_json(message):
            json_msg = json.loads(message.decode("utf-8"))
            json_msg["board"][0] = "2"
            json_msg = json.dumps(json_msg)
            message = bytes(json_msg, "utf-8")
        
        print("Recieved message", message)
        if (message):
            print("sending")
            c.send(message)
            message = None
        print("type 'stop' to quit server, press enter to keep recieving")
        if (input() == "stop"):
            break

# receive data from the server 

# close the connection 
    c.close()

"""