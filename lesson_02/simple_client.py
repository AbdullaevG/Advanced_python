import socket
import pickle

def client_program():
    port = 8010  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect(("127.0.0.1", port))  # connect to the server

    message = "https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BB%D0%B8%D0%BD%D0%B0"  # take input

    while len(message) > 0:
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024) # receive response
        data = pickle.loads(data)
        #print('Received from server: ' + data)  # show in terminal
        with open("result.txt", "a") as file:
            file.write(message + "\n")
            file.write(data)
            file.write(3*"\n")
        message = ""  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()