from Board import *

from OFF_Data import *
from OFF_Network import *

from GameLogic import *

# Assume we're using SERVER_INFO for all of these requests
def send_message(message, sourceSocket):
    request = serialize_data(message)
    response = send_comm(request, sourceSocket, SERVER_INFO)
    return response

def display_side_by_side(plyrBoard, enemyBoard):
    # Change it so that they're always some minimum distance apart?
    print("Player 1                                 Player 2")
    for i in range(0, plyrBoard.height):
        print(str(plyrBoard.grid[i]) + "  " + str(enemyBoard.grid[i]))

# Add functionality to reconnect...?
# Same SERVER_INFO is assumed... as always
def connect_to_server(plyrSocket):
    connectRequest = {'msg' : 'Connect'}
    #serialMsg = serialize_data(rawMsg)
    response = send_message(connectRequest, plyrSocket)

    # Do I need to deserialize it?
    #deserialResponse = deserialize_data(response)

    '''
    # If we're player 1, then up the parameters
    if serverResponse['msg'] == "Set_Parameters":
        parameters = {'Height': 0, 'Width' : 0, 'Mines' : 0}

        parameters['Height'], parameters['Width'], parameters['Mine'] = game_input()

        serialParam = serialize_data(parameters)
        send_comm(serialParam, sourceSocket, SERVER_INFO)
        # Don't get a response yet, we have to wait for the other player
        # to connect first?

    return deserializeResponse
    '''
