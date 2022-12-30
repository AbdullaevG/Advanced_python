# Import socket module
import socket            
import pickle

# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 8006               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))

# The client send this line to server
urls_file_path = "./data/urls.txt"
# receive data from the server and decoding to get the string.


def get_url_from_file(file_path = urls_file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            yield line


for temp_url in get_url_from_file():
    data = []
    s.send(temp_url.encode())
    packet = 1
    while packet:
        packet = s.recv(1024)
        print(pickle.loads(packet)
        if not packet: break
        message = packet
        data.append(packet)
    print("data is accepted")
        
    data_arr = pickle.loads(b"".join(data))   
    with open("client_data.txt", "a", encoding="utf-8") as output_file:
        for item in data_arr:
            output_file.write(str(item[0]) +": " + str(item[1]) + "\n")
        print("result is written")
    #print(message.decode())
#print(s.recv(1024).decode())
#print(s.recv(1024).decode())
# close the connection
s.close()