"""@package docstring
GameClient.py deals with client specific functionality such as:
    Update player data
    Provide an interface for network communication
    And... other stuff
"""

# By importing OFF_Network we should have access to all of the server
import OFF_Network

def receive_data():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto("hi".encode(), serverInfo)
    serData, serverAddress = clientSocket.recvfrom(2048)

    return serData
