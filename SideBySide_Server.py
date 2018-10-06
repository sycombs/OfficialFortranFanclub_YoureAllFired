from Board import *
from OFF_Data import *
from OFF_Network import *

''' TODO: Find a way to deal with buffers getting too large?
'''

def generate_board(parameters):
    serverGeneratedBoard = Board(parameters['height'],
                                    parameters['width'],
                                    parameters['mines'])
    return serverGeneratedBoard


plyr1Board = generate_board(parameters)
plyr1MoveBuffer = {'Move1': '',
                'Move2': '',
                'Move3': '',
                'Move4': '',
                'Move5': '',
                'Move5': '',
                'Move6': '',
                'Move7': '',
                'Move8': '',
                'Move9': '',
                'Move10': ''}


plyr1Board = generate_board(parameters)
plyr2MoveBuffer = {'Move1': '',
                'Move2': '',
                'Move3': '',
                'Move4': '',
                'Move5': '',
                'Move5': '',
                'Move6': '',
                'Move7': '',
                'Move8': '',
                'Move9': '',
                'Move10': ''}


playerCount = 0

# Wait for two players to connect
#while playerCount == 0:

# When one player connects, let them start a game normally
# THE PLAYER HAS TO BE STOPPED FROM PLAYING UNTIL SOMEONE ELSE CONNECTS


# Server functions go here!?
def respond_to_message(serialMsg, sender):
    msg = deserialize_data(serialMsg)

    if msg['Message'] == 'NewBoard':
        # Flush the player's buffer

        # Generate and send a new board
        newBoard = generate_board(parameters)

    if msg['Message'] == 'Win':
        # Do win stuff
        print("Congrats")

    if msg['Message'] == "Action"
        add_to_buffer(msg['ID'], msg['moveMade'])
        # Send a response to the player...
        # Send the other player's buffer or new board...
        if msg['ID'] == 1:
            print("Sending player 2 stuff")
        if msg['ID'] == 2:
            print("Sending player 1 stuff")

    # Only let people set parameters on their connect
    #if msg['Message'] == 'SetParam':
