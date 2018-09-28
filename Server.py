# Server testing
from socket import *
import pickle
import Client


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))


''' WHEN A GAME IS FIRST RUN THE SERVER ASKS WHAT KIND OF THE GAME THE PLAYER
    WOULD LIKE TO PLAY. AT THIS POINT IT IS _REQUIRED

    When a game is first run the server asks what kind of the game the player
    would like to play. At this point in development it will be REQUIRED
    that a server be running in order to play unless we add a way for the Play
    method to circumvent that and start up normally
'''

# On initial connect
''' WE ARE JUST USING BOOL'S FOR NOW,
LATER ON WE CAN SEND DIFFERENT DATA TYPES... LIKE MAYBE A BOOL '''

gameRunning = False

while gameRunning == False:
    gameRequest, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)
    if gameRequest.decode() == 'SP': #Single Player
        gameType = 'SP'
        gameRunning = True
        serverSocket.sendto(("START").encode(), clientAddress)

    else:
        serverSocket.sendto('Write SP'.encode(), clientAddress)

''' GAME STATUS STUFF '''
#gameType = '' # DON'T START WRITING THINGS TWICE


# If a player has won, tell everyone from now on to stop playing
gameOver = False
cPlayers = 0




print("Minesweeper server is now active")

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
