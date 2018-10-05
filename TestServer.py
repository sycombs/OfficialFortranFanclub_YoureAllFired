'''
MY TEST SERVER FOR NOW
'''
from OFF_Data import *
from OFF_Network import *

from GameLogic import *

# Server Init
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', SERVER_PORT))

# Board Init
tB = Board(10, 10, 1)

while True:
    dataSerial, clientAddress = serverSocket.recvfrom(2048)

    a = tB.get_string_rep()
    newDataSerial = serialize_data(a)
    send_comm(newDataSerial, serverSocket, clientAddress)
    #response = send_comm(newDataSerial, serverSocket, clientAddress)
    #print(response)
