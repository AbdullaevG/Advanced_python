import socket
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import re
import pickle

def get_n_often_words(url, n = 10):
    """Get text from url and return n offten words in text"""
    
    # get html document
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features = "html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    # get text from body
    text = soup.body.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    # words counter
    counter = Counter()
    # remove puctuations
    all_words = re.findall(r"\w+", text.lower())
    words = []
    # remove prepositions
    for word in all_words:
        if len(word) > 2:
            words.append(word)
    counter.update(words)
    most_common = counter.most_common(n)
    
    return str(most_common)


def server_program():
    # get the hostname
    port = 8011  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(("", port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        
        url = conn.recv(4096).decode()
        if not url:
            # if data is not received break
            break
        print("from connected user get url: ", url)
        data = get_n_often_words(url, n = 10)
        data  = pickle.dumps(data)
        conn.send(data)  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()