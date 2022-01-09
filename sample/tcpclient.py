
# Import socket module
import socket            
 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('192.168.88.148', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()    
     