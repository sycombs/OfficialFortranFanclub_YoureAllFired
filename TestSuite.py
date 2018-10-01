"""@package docstring
Testing suite
I'm just keeping this file around in order to be able to test out whatever
is necessary
"""

# Testing node.js server stuff
import requests
from socket import *
import json

#r = requests.get('https://localost:8080/winter')
#print(r)

serverName = '127.0.0.1'
serverPort = 3000

serverInfo = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_DGRAM)

# Try sending the data, and if it doesn't work then print some error


# Player stuff
#from player import *

#testPlayer = Player()
#testPlayer.send_player_state()
