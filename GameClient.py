"""@package docstring
GameClient.py
"""

''' TODO:
    1) Include proper exceptions for try-catch blocks
         Sections where this is required are flagged with # HERE
    2) Change 'from socket import *' to 'import socket' and fix any resultant
    issues
    3) Remove hardcoded server data?
'''

# socket allows communication with a server
from socket import *

# json is used to serialize data
import json

# Server Data
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Store the data as a tuple (?) just to make things look cleaner later on
serverInfo = (serverName, serverPort)

def send_to_server(rawData):
    """
    Serialize the data using JSON, then send it to the server and close
    the socket
    """

    try:
        serializedData = json.dumps(self.rawData)
    except: # HERE
        print("Error when converting to json format")


    # Create a socket
    #clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Try sending the data, and if it doesn't work then print some error
    try:
        clientSocket.sendto(pData.encode(), serverInfo)
        clientSocket.close()

    except Exception as e:
        print(e)

def get_board():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto("hi".encode(), serverInfo)
    serData, serverAddress = clientSocket.recvfrom(2048)

    return serData

def receive_data():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto("hi".encode(), serverInfo)
    serData, serverAddress = clientSocket.recvfrom(2048)

    return serData
'''
    try:
        serData, serverAddress = cSocket.recvfrom(2048)
        print(serData.decode())
        return serData
    except Exception as e:
        print(e)
        waitingForData = False
        #if serData != None:
            #waitingForData = False
    try:
        rawData = pickle.loads(serData)
        print("Received pickle data")
        return rawData
    except Exception as e:
        print(e)
        return
'''


#def receive_board()
