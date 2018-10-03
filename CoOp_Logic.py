# Multiplayer stuff
# Server and game logic stuff


'''
MY TEST SERVER FOR NOW
'''
from Server import *
from GameLogic import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
player_count = 0
set_game_params = False
while True:
    rawData, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)

    useable_data = interpret_data(rawData)
    #since the entire thing runs in a loop, check if params are set
    if set_game_params == False:
        serverSocket.sendto("inp".encode(), clientAddress)
        rawData, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)
        player_state = interpret_data(rawData)
        #this takes the string tuple in playerdata['msg'] converts to board
        board_tuple = tuple(map(int,player_state['msg'].split(' ')))
        board = Board(board_tuple[0],board_tuple[1],board_tuple[2])
        send_board(serverSocket,clientAddress,board)

    serverSocket.sendto("Okay".encode(), clientAddress)

#a = True

# Try sending a Board
#while (a == True):
    # Get a message
#    data, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)

    # Send a board in response
#    sendBoard = Board(2, 2, 1)

    #pBoard = pickle.dumps(sendBoard)
    #serverSocket.sendto(pBoard, clientAddress)

    #a = False




'''
while True:
    # Receive request
    data, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)
    serverSocket.sendto(.encode(), clientAddress)
    #serverSocket.sendto("Response 2".encode(), clientAddress)

    if isinstance(data, str):
        try:
            print("It's a string")
            interpret_data(data)
        except Exception as e:
            print(e)

    #serverSocket.sendto("Response".encode(), clientAddress)
'''

# *** WAITING FOR PLAYER 1 TO CONNECT ***

# Current player count: 0

# PLAYER CONNECTED
    # Increase player count to 1
    # Give that player an ID# and put them in charge of the board creation

# Assume evreything worked...

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
