# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
  
# Define the port on which you want to connect 
port = 12346                
  
# connect to the server on local computer 
s.bind(('127.0.0.1', port)) 

s.listen(5)
while True:
    c, addr = s.accept()
    print("Connection established!")
    message = c.recv(1024)
    print("Recieved message", message)
    if (message):
        print("sending")
        c.send(message)
        message = None


# receive data from the server 

# close the connection 
c.close()
