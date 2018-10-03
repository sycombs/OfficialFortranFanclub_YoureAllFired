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


# Server Data
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Store the data as a tuple (?) just to make things look cleaner later on
serverInfo = (serverName, serverPort)

def send_data(rawData):
    """
    send_data() will... not have to check the type of data we're sending?

    It seems like the sockets module does a pretty good job of taking care of
    sending data over regardless
    """

    try:
        serializedData = json.dumps(self.rawData)
    except Exception as e:
        print(e)


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
