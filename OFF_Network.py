"""@package docstring
Official Fortran Fanclub Network Module

"""
# Socket allows us to create and deal with networks
from socket import *

# I don't like this... I wanted to keep things separate, but time is off
# the essence and not doing this is sort of annoying :(
from OFF_Data import *


# Get and print the local network address
localAddress = gethostbyname(gethostname())
#SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT    = 12000

SERVER_INFO = (localAddress, SERVER_PORT)

''' NETWORK COMMUNICATION FUNCTIONS '''



def send_byte_data(byteData, sourceSocket, destination):
    """
    send_byte_data() sends <type: bytes> to some destination. It does not
    accept return data
    """
    try:
        sourceSocket.sendto(byteData, destination)
    except Exception as e:
        print("ERROR IN send_byte_data")
        print("CAUSED BY: " + str(byteData))
        print(e)

def send_string_data(strData, sourceSocket, destination):
    """
    send_string_data() sends <type: string> to some destination. It does not
    accept return data
    """
    try:
        sourceSocket.send(strData, destination)
    except Exception as e:
        print("ERROR IN send_string_data")
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
            #print("GOT A RESPONSE")
            return response
    except Exception as e:
        print(e)

''' I realized it'll quickly get very annoying to manually (de)serialize data
    so often so... use this when you don't want to do all of that
'''
'''
def nice_send_comm(rawData, sourceSocket, destination):
    """
    send_raw_comm() serializes and then sends data using... serialize_data and
    send_comm
    """
    data = serialize_data(rawData)

    try:
        # Send the data
        #sourceSocket.sendto(data, destination)
        send_comm(data, sourceSocket, destination)

        # Return the response. We keep senderAddress because... ... ...!
        #response, senderAddress = sourceSocket.recvfrom(2048)
        return deserialize_data(response)

    except Exception as e:
        print(e)
'''
