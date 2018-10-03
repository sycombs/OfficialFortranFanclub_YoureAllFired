# Official Fortran Fanclub Network module

# Socket allows us to create and deal with networks
import socket

# JSON and pickle allow us to serialize game data
import json
import pickle

# I suspect we'll stick with the same server address and port number for a while
# so I'm going to set those here
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT    = 12000

SERVER_INFO = (SERVER_ADDRESS, SERVER_PORT)

''' TRANSMISSION FUNCTIONS '''
'''
def send_obj(serverSocket, clientAddress, rawData):
    """
    send_obj() sends pickled object data
    """
    try:
        pickleData = pickle.dumps(rawData)
        serverSocket.sendto(pickleData, clientAddress)
    except Exception as e:
        print(e)

def send_json(serverSocket, clientAddress, rawData):
    """
    send_json() sends json data
    """
    try:
        jsonData = json.dumps(rawData)
        serverSocket.sendto(jsonData, clientAddress)
    except Exception as e:
        print(e)
'''
def send_comm(data, sourceSocket, destination):
    """
    send_comm() sends a <type: Generic> message to some destination and then
    (for my sake) prints out the sender's response

    I say for my sake because it means I don't want to deal with craziness again
    """
    try:
        sourceSocket.sendto(data, destination)

        response, senderAddress = sourceSocket.recvfrom(2048)
        print("Sender Response: " + response.decode())

    except Exception as e:
        print(e)
