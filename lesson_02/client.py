# Import socket module
import socket            
import pickle
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 8002               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
# The client send this line to server
urls_file_path = "./data/urls.txt"
s.send(urls_file_path.encode())
# receive data from the server and decoding to get the string.
data = []
while True:
    packet = s.recv(4096)
    if not packet: break
    data.append(packet)
data_arr = pickle.loads(b"".join(data))
print(data_arr)
with open("client_data.txt", "a", encoding="utf-8") as output_file:
    output_file.write(str(data_arr))


print(s.recv(1024).decode())
# close the connection
s.close()