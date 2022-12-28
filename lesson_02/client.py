# Import socket module
import socket            
import pickle

# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 8005               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))

# The client send this line to server
urls_file_path = "./data/urls.txt"
s.send(urls_file_path.encode())
# receive data from the server and decoding to get the string.
data = []
packet = 1
while True:
    packet = s.recv(1024)  
    if not packet: break
    message = packet
    data.append(packet)
    data_arr = pickle.loads(b"".join(data))
    
    with open("client_data.txt", "w", encoding="utf-8") as output_file:
         for item in data_arr:
                output_file.write(str(item[0]) +": " + str(item[1]) + "\n")

    #print(message.decode())
#print(s.recv(1024).decode())
#print(s.recv(1024).decode())
# close the connection
s.close()