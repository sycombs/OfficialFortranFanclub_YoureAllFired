"""@package docstring
I don't know yet...
"""


''' TODO: Remove the client specific code from the Player class and move it
elsewhere. The client should only be involved in the sending and receiving of
data but should not interpret any of the data past calling the proper functions
in response to what was received

GameClient.py should handle the serialization of data. That way the Player
class is kept separate from the network implementation. This allows us to
change the player data pretty quickly and easily since all we have to do is
pass the data and not worry much about how it's formatted or how it's sent
'''

from socket import *
import json


serverName = '127.0.0.1'
serverPort = 12000

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
        '''
        We can change this to a simple get function and then pass the data
        to the GameClient function that's in charge of sending data
        '''

        # This will serialize the data using the JSON format
        pData = json.dumps(self.playerData)

        # Create a socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        # Try sending the data, and if it doesn't work then print some error
        try:
            clientSocket.sendto(pData.encode(), serverInfo)
            response, serverAddress = clientSocket.recvfrom(2048)
        except Exception as e:
            print(e)

        
        print(type(response))
                #print("I call create stuff here")

            # Make sure to close the socket after we received the data
            #clientSocket.close()
