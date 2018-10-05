'''
MY TEST SERVER FOR NOW
'''
from OFF_Data import *
from OFF_Network import *

from GameLogic import *

#def get_string_rep():




# Server Init
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', SERVER_PORT))

# Board Init
tB = Board(10, 10, 1)


while STAGE_1:
    dataSerial, clientAddress = serverSocket.recvfrom(2048)

    # Assuming we only get here after we received something...
    playerCount = playerCount + 1 # Will this help prevent errors?

    # Decode the info and change it
    dataDeserial = deserialize_data(dataSerial)
    dataDeserial['ID'] = playerCount

    # Serialize it and send it back
    newDataSerial = serialize_data(dataDeserial)
    send_comm(newDataSerial, serverSocket, clientAddress)

    # Exit out
    STAGE_1 = False
