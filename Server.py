"""@package docstring
Server.py contains all of the game server functionality. A server should
    1) Be created
    2) Listen for incoming messages
    3) Interpret messages and call other code as necessary

Server.py should not be used to run a server, any instances of a server
should be created in Play.py . Server.py does not handle game logic either, it
only facilitates the communication between the client (where the user interacts)
and the server (where the game specific code is handled).

We may not run a pure client-server model so keep that in mind when moving
code out of this file... like the server loop
"""

''' TODO: Remove the instance of a server loop from here and place it elsewhere
'''


# Server Imports
from socket import *
from Board import *
import pickle

import json

# Server Data
serverPort = 12000
#serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind a server
#serverSocket.bind(('', serverPort))

def interpret_data(data):
    """
    This will be used to deserialize the received data. Once that's done, the
    kind of data we have will determine what's done next
    """

    '''
    Data received should be easily convertable. The following has a table
    with the encode / decode formats for  JSON to Python
    https://docs.python.org/3/library/json.html#json-to-py-table
    '''

    try:
        # Deserialize the data and then print it to the console so we can
        # see what's being received
        deserializedData = json.loads(data)
        return deserializedData

    except Exception as e:
        print(e)


def send_board(serverSocket, clientAddress, rawData):
    try:
        pickleData = pickle.dumps(rawData)
        serverSocket.sendto(pickleData, clientAddress)
    except Exception as e:
        print(e)

def send_json(serverSocket, clientAddress, rawData):
    try:
        jsonData = json.dumps(rawData)
        serverSocket.sendto(jsonData, clientAddress)
    except Exception as e:
        print(e)

def send_data(serverSocket, clientAddress, rawData):
    try:
        serverSocket.sendto(pickleData, clientAddress)
    except Exception as e:
        print(e)

    if isinstance(rawData, Board):
        try:
            print("Sending a board")
            send_board(serverSocket, clientAddress, rawData)
        except:
            print("Type: Board, had issue in send_data")

    elif isinstance(rawData, str):
        try:
            print("Sending json")
            send_json(serverSocket, clientAddress, rawData)
        except:
            print(e)

    else:
        print("Error, could not determine type")
