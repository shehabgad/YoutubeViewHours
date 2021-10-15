import json
import socket
import json
import selenium

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 28000))
size = 10485760


youtubeLinks = s.recv(size)
youtubeLinks = json.loads(youtubeLinks.decode())
for i in range(len(youtubeLinks)):
    print(youtubeLinks[i])
input("closeConnection")
s.close()
