import json
import socket
import json
import selenium

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect_ex(("172.26.9.86", 28000))
size = 10485760


youtubeLinks = s.recv(size)
youtubeLinks = json.loads(youtubeLinks.decode())

for i in range(len(youtubeLinks)):
    print(youtubeLinks[i])
input("closeConnection")
s.close()
