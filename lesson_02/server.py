# first of all import library
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
        if len(word) > 1:
            words.append(word)
    counter.update(words)
    most_common = counter.most_common(n)
    
    return most_common
    
    
# create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 8005 but it can be anything
port = 8006               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network

s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening...")           
 
# a forever loop until we interrupt it or
# an error occurs
recived_path = 1
c, addr = s.accept()
print ('Got connection from', addr)

while recived_path:
    # Establish connection with client.  
    print ('Got connection from', addr)
    recived_path = c.recv(4096).decode()
    print(recived_path)
    top_10 = get_n_often_words(recived_path.strip())
    data  = pickle.dumps(top_10)
    c.send(data)
    print("data is sended")

s.closed()
