"""@package docstring
GameClient.py
"""

''' TODO:
    1) Include proper exceptions for try-catch blocks
         Sections where this is required are marked with # HERE
    2) Change 'from socket import *' to 'import socket' and fix any resultant
    issues
    3) Remove hardcoded server data?
'''

# socket allows communication with a server
from socket import

# json is used to serialize data
import json

# Server Data
serverName = '127.0.0.1'
serverPort = 12000

# Store the data as a tuple (?) just to make things look cleaner later on
serverInfo = (serverName, serverPort)

def send_to_server(rawData):
    try:
        serializedData = json.dumps(self.rawData)
    except: # HERE
        print("Error when converting to json format")


    # Create a socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Try sending the data, and if it doesn't work then print some error
    try:
        clientSocket.sendto(pData.encode(), serverInfo)
        clientSocket.close()
    except: # HERE
        print("Error transmitting data to server")
