# Server testing
from socket import *
import pickle
import Client


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server is ready to receive")


# If a player has won, tell everyone from now on to stop playing
gameOver = False

cPlayers = 0

while True:
    # Receive the data
    data, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)

    if gameOver:
        msg = "It's over. You lost."
        serverSocket.sendto(msg.encode(), clientAddress)

    # Check which type of data we have
    try:
        # Try to decode the data. If it's a string, it will work
        msg = data.decode()
        if msg == "WIN":
            gameOver = True
            serverSocket.sendto("Congratulations".encode(), clientAddress)
        else:
            serverSocket.sendto("Keep trying".encode(), clientAddress)

    except:
        print("Error, sent complexData")

    try:
        # Try to unpickle the data
        uPick = pickle.loads(data)
        uPick()
    except:
        print("Error, things didn't work out well")
        #serverSocket.sendto(str(thing).encode(), clientAddress)
