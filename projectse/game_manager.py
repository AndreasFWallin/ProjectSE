import socket
""" Proxy module which handles the communication between Game Engine and Game Platform modules """
class EngineManager:
    def __init__(self, ip_adress='192.168.56.1', port=12346):
        self.socket = socket.socket()           # Allocating a socket 
        self.socket.connect((ip_adress, port))  # Connecting the socket to a
        print("Connection to server established")

    def send(self, message):
        """
        A function for turning a message into bytes and then send it 
        """
        message_b = bytes(message)            # Convert the message to bytes
        print(message_b)
        self.socket.send(message_b)           # Send the game state/move
        print("Message sent!")
        
    def recv(self):
        """
        A function for recieving a message 
        """
        message_recieved = self.socket.recv(1024)
        # TODO add the necessary transformation of the data
        print("message_recieved", message_recieved)
        return message_recieved
    
    def close(self):
        """
        A function for sending and rec
        """
        self.socket.close()
        print("Socket closed")

