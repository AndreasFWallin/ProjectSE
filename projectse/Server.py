# Import socket module 
import socket
import json                
  
def is_json(myjson):
    """
    checking to see if a file is a json
    """
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
  
# Define the port on which you want to connect 
port = 3005    
  
# connect to the server on local computer 
s.bind(('192.168.0.101', port))

s.listen(5)
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

