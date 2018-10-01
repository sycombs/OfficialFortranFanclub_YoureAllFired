"""@package docstring
I don't know yet...
"""

from socket import *
import json


serverName = '127.0.0.1'
# Running node.js on port 3000
serverPort = 3000

serverInfo = (serverName, serverPort)

class Player:
    def __init__(self):
        """
        Doxygen Comments Doxygen Comments Doxygen Comments
        """

        '''
        When creating any sort of player data, look at the following in order
        to make sure it's formatted properly so that we can send it via JSON
        https://docs.python.org/3/library/json.html#json-to-py-table

        (Just make sure to use a dictionary, string, or int and and everything
        will work fine)
        '''
        self.playerData = {'ID': 0, 'msg': 'Just a message', 'win': False}

    def send_player_state(self):
        """
        Serialize the data using JSON, then send it to the server and close
        the socket
        """

        # This will serialize the data using the JSON format
        pData = json.dumps(self.playerData)

        # Create a socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        # Try sending the data, and if it doesn't work then print some error
        try:
            clientSocket.sendto(pData.encode(), serverInfo)
            clientSocket.close()
        except:
            print("Error sending data")
