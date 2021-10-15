import socket
import threading
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 28000))


def vpsConnection(so, arr):
    data = json.dumps(arr)
    so.send(data.encode())


n = 0
vpsSockets = []
nvps = int(input("how many vps will be connected ?"))
for i in range(nvps):
    s.listen(5)
    vpsSocket, address = s.accept()
    vpsSockets.append(vpsSocket)
    n += 1
    print(f" there is {n} vps connected")

while True:
    youtubeLinks = []
    numberOfLinks = int(input("how many youtube links ?"))
    for i in range(numberOfLinks):
        youtubeLink = input(f"Enter link {i + 1}: ")
        youtubeLinks.append(youtubeLink)
    for i in range(len(vpsSockets)):
        vpsConnection(vpsSockets[i], youtubeLinks)

s.close()
