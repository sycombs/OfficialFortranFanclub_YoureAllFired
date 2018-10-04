"""@package docstring
GameClient.py
"""

# By importing OFF_Network we should have access to all of the server
import OFF_Network


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
