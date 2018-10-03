"""@package docstring
Testing suite
I'm just keeping this file around in order to be able to test out whatever
is necessary
"""


from socket import *
import json
import pickle

# Player stuff
from player import *

from Board import *
import GameClient


# Test:
'''
player: Send data to the server
player: Receive data from the server

Server: Work!
'''

#testPlayer = Player()
#testPlayer.send_player_state()
#print("Done with player stuff")



# Send the player data
# Get a response

#fuck = True

#while (fuck == True):
    #clientSocket = socket(AF_INET, SOCK_DGRAM)
    #clientSocket.sendto("hi".encode(), serverInfo)
    #serData, serverAddress = clientSocket.recvfrom(2048)

    #uData = pickle.loads(serData)
    #uData.displayBoard()


#aB = GameClient.receive_data().decode()
#print(aB)
#bB = pickle.loads(aB)
#bB.displayBoard()

#send_to_server(rawData):

import random



plyr1 = Player()
plyr1.playerData['ID'] = 1
#plyr1.send_player_state()

plyr2 = Player()
plyr2.playerData['ID'] = 2
#plyr2.send_player_state()

playerArray = [plyr1, plyr2]

while True:
    n = random.randint(0, 1)

    playerArray[n].send_player_state()
    
