import socket
import pickle

URLS_FILE = "urls.txt"

def read_urls(urls_file=URLS_FILE):
    url_list = []
    with open(urls_file) as file:
        for line in file:
            url_list.append(line.strip())
    return url_list

def client_program():
    port = 8011  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect(("127.0.0.1", port))  # connect to the server

    url_list = read_urls(urls_file=URLS_FILE)
    url_list.append("")
    num_files = len(url_list)
    for url in url_list:
        if len(url) == 0:
            break
        client_socket.send(url.encode())  # send message
        data = client_socket.recv(4096) # receive response
        data = pickle.loads(data)
        #print('Received from server: ' + data)  # show in terminal
        with open("result.txt", "a") as file:
            file.write(url + "\n")
            file.write(data)
            file.write(3*"\n")
    print("Client closed")
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()