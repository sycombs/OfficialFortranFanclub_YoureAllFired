from NetPlayer import *
from Board import *

from OFF_Data import *
from OFF_Network import *

# Assume we're using SERVER_INFO for all of these requests
def send_message(message, sourceSocket):
    request = serialize_data({'Message': message})
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
    rawResponse = send_message("Connect", plyrSocket)

    # Do I need to deserialize it?
    deserialResponse = deserialize_data(rawResponse)

    if serverResponse == "Set_Parameters":
        # Add the request parameter stuff here...
        # Assign player values
        print("A")

    #if serverResponse == ""
