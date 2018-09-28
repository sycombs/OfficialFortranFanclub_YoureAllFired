# Server testing
from socket import *
import pickle
import player


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server is ready to receive")


# Determine the player's position

cPlayers = 0

while True:
    # Receive the data
    data, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)

    # Check which type of data we have
    try:
        # Try to decode the data. If it's a string, it will work
        msg = data.decode()
        print(msg)
    except:
        print("Error, sent complexData")

    try:
        # Try to unpickle the data
        uPick = pickle.loads(data)
        uPick()
    except:
        print("Error, things didn't work out well")
        #serverSocket.sendto(str(thing).encode(), clientAddress)
