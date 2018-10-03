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

import pickle

import json

# Server Data
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind a server
serverSocket.bind(('', serverPort))

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
        print(deserializedData)

    except JSONDecodeError as e:
        print(e)


def send_board(clientAddress, rawData):
    serializedData = pickle.dumps(rawData)
    serverSocket.sendto(serializedData, clientAddress)


def send_data(clientAddress, rawData):
    if isinstance(rawData, Board):
        try:
            send_board(clientAddress, rawData)
        except:
            print("Type: Board, had issue in send_data")

    elif isinstance(rawData, str):
        try:
            send_json(clientAddress, rawData)
        except:
            print("Type: str, had issue in send_data")

    else:
        print("Error, could not determine type")


''' SERVER LOOP - PLACE ELSEWHERE'''
while True:
    # Receive the data
    data, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)

    interpret_data(data)
