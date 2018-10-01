"""@package docstring
Server.py handles sending and receiving data, but based on that data
it will load up the necessary rules to handle the game itself... bad comment
"""

# Server testing
from socket import *
import json


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
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
        deserializedData = json.loads(data)
        print(data)

        # Server side print so we can see what's being received
        print(deserializedData)

    except JSONDecodeError as e:
        print(e)


cPlayers = 0


''' SERVER LOOP '''
while True:
    # Receive the data
    data, clientAddress = serverSocket.recvfrom(2048 * 2 * 2 * 2)

    interpret_data(data)
