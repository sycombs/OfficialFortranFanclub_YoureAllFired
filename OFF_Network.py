"""@package docstring
Official Fortran Fanclub Network Module

"""
# Socket allows us to create and deal with networks
from socket import *

# I don't like this... I wanted to keep things separate, but time is off
# the essence and not doing this is sort of annoying :(
from OFF_Data import *

# I suspect we'll stick with the same server address and port number for a while
# so I'm going to set those here
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT    = 12000

SERVER_INFO = (SERVER_ADDRESS, SERVER_PORT)

''' NETWORK COMMUNICATION FUNCTIONS '''

def send_byte_data(byteData, sourceSocket, destination):
    try:
        sourceSocket.sendto(byteData, destination)
    except Exception as e:
        print("ERROR: send_byte_data() in OFF_Network.py")
        print("CAUSED BY: " + str(byteData))
        print(e)

def send_string_data(strData, sourceSocket, destination):
    try:
        sourceSocket.send(strData, destination)
    except Exception as e:
        print("ERROR: send_string_data() in OFF_Network.py")
        print("CAUSED BY: " + str(strData))
        print(e)


def send_comm(data, sourceSocket, destination, requiresResponse = None):
    """
    send_comm() sends a <type: Generic> message to some destination and then
    (for my sake) prints out the sender's response

    I say for my sake because it means I don't want to deal with craziness again
    """

    try:
        sourceSocket.sendto(data.encode(), destination)
        # Return the response. We keep senderAddress because... ... ...!
        #print("WAITING FOR A RESPONSE")

        if requiresResponse:
            response, senderAddress = sourceSocket.recvfrom(2048)
            return response
    except Exception as e:
        print("ERROR: send_comm() in OFF_Network.py")
        print(e)
