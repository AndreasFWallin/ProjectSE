import socket


""" Proxy module which handles the communication between Game Engine and Game Platform modules """
class GameManager:
    def __init__(self, ip_adress='192.168.0.105', port=12346):
        """
        Sets up the connection, if the creation of the game manager doesn't work
        make sure you are on the same networ, have the same ip and port on server and manager
        """
        self.socket = socket.socket()           # Allocating a socket 
        self.socket.connect((ip_adress, port))  # Connecting the socket to a server, given an ip and port
        print("Connection to server established")

    def send(self, message):
        """
        A function for turning a message into bytes and then send it,
        the message has to be converted at the destination, e.g str(message, 'utf-8').
        """
        message_b = bytes(message)            # Convert the message to bytes
        print(message_b)
        self.socket.send(message_b)           # Send the game state/move
        print("Message sent!")
        
    def recv(self, dtype = "np_array"):
        """
        A function for recieving a message 
        """
        message_recieved = self.socket.recv(1024)
        if dtype == "np_array":
            message_recieved = list(message_recieved)
        # TODO add the necessary transformation of the data
        elif dtype == "string":
            message_recieved = message_recieved.decode()
        else:
            print("Warning, incorrect option")
            exit(0)
        print("message_recieved", message_recieved)
        return message_recieved
    
    def close(self):
        """
        Closes the connection
        """
        self.socket.close()
        print("Socket closed")

