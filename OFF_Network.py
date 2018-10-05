"""@package docstring
Official Fortran Fanclub Network Module

"""
# Socket allows us to create and deal with networks
from socket import *

# I don't like this... I wanted to keep things separate, but time is off
# the essence and not doing this is sort of annoying :(
from OFF_Network import *

# I suspect we'll stick with the same server address and port number for a while
# so I'm going to set those here
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT    = 12000

SERVER_INFO = (SERVER_ADDRESS, SERVER_PORT)

''' NETWORK COMMUNICATION FUNCTIONS '''

def send_comm(data, sourceSocket, destination):
    """
    send_comm() sends a <type: Generic> message to some destination and then
    (for my sake) prints out the sender's response

    I say for my sake because it means I don't want to deal with craziness again
    """
    try:
        # Send the data
        sourceSocket.sendto(data.encode(), destination)

        # Return the response. We keep senderAddress because... ... ...!
        response, senderAddress = sourceSocket.recvfrom(2048)
        return response

    except Exception as e:
        print(e)

''' I realized it'll quickly get very annoying to manually (de)serialize data
    so often so... use this when you don't want to do all of that
'''

def nice_send_comm(rawData, sourceSocket, destination):
    """
    send_raw_comm() serializes and then sends data using... serialize_data and
    send_comm
    """
    data = serialize_data(rawData)

    try:
        # Send the data
        sourceSocket.sendto(data.encode(), destination)

        # Return the response. We keep senderAddress because... ... ...!
        response, senderAddress = sourceSocket.recvfrom(2048)
        return deserialize_data(response)

    except Exception as e:
        print(e)
