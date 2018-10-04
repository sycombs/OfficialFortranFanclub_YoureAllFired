# Multiplayer stuff
# Server and game logic stuff


'''
MY TEST SERVER FOR NOW
'''
import OFF_Data
from OFF_Network import *

from GameLogic import *


STAGE_1 = True
STAGE_2 = False
MAIN_LOOP = False


# *** WAITING FOR PLAYER 1 TO CONNECT ***

# Current player count: 0
playerCount = 0

# PLAYER CONNECTED
    # Increase player count to 1
    # Give that player an ID# and put them in charge of the board creation

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', SERVER_PORT))

while STAGE_1:
    message, clientAddress = serverSocket.recvfrom(2048)
//
#while STAGE_1:
    #message, clientAddress = serverSocket.recvfrom(2048)

# Assume everything worked...

# *** WAITING FOR PLAYER 2 TO CONNECT ***

# Current player count: 1

# PLAYER 2 CONNECTED
    # Show the player the board player 1 generated
    # Ask the player if they like what they see

    # PLAYER LIKES IT
    # Increase player count to 2

# START THE GAME!

# *** GAME STARTED ***

# Send both players the most recent board
# Ask current player for input

# WAITING FOR PLAYER INPUT
    # Start turn timer
    # Player submits move?
        #Verify move is valid (or quit?)

# PLAYER INPUT DECLINED
    # Tell them it's invalid

# PLAYER INPUT ACCEPTED
    # Update board and states
    # Change current player
    # Start process again
