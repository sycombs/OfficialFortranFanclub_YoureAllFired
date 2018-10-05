'''
MY TEST SERVER FOR NOW
'''
from OFF_Data import *
from OFF_Network import *

from GameLogic import *



# Board Init
tB = Board(10, 10, 1)

playerCount = 0

#a = tB.get_string_rep()
#newDataSerial = serialize_data(a)
#send_comm(newDataSerial, serverSocket, clientAddress)
#response = send_comm(newDataSerial, serverSocket, clientAddress)
#print(response)


# Server Init
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', SERVER_PORT))

print("Server window")

STAGE_1 = True

playerTurn = 1

while STAGE_1:
    dataSerial, clientAddress = serverSocket.recvfrom(2048)

    dataDeserial = deserialize_data(dataSerial)
    print("Request from player " + str(dataDeserial['ID']))
    print("Current turn belongs to: " + str(playerTurn))

    # Assuming we only get here after we received something...
    #playerCount = playerCount + 1 # Will this help prevent errors?

    # Decode the info and change it
    #dataDeserial = deserialize_data(dataSerial.decode())

    if int(dataDeserial['ID']) != playerTurn:
        msg = "IT'S NOT YOUR TURN YET"
        send_comm(msg, serverSocket, clientAddress, False)

    else:
        #dataDeserial['ID'] = playerCount

        # Send a hello message
        msg = "You're so beautiful"
        send_comm(msg, serverSocket, clientAddress, False)

        # Serialize it and send it back
        #newDataSerial = serialize_data(dataDeserial)
        #send_comm(newDataSerial, serverSocket, clientAddress, False)

        # Start listening for a new request
        dataSerial, clientAddress = serverSocket.recvfrom(2048)

        # TRYING TO SEND A BOARD!
        #serverSocket.sendto("Got a request".encode(), clientAddress)

        # Serialize the board and send it
        a = tB.get_string_rep()
        s = serialize_data(str(a))
        #print("Type a is: " + str(type(a)))

        serverSocket.sendto(s.encode(), clientAddress)
        #result = send_comm(a, serverSocket, clientAddress, False)
        #if result != None:
            #print(result)
        if playerTurn == 1:
            playerTurn = 2
        elif playerTurn == 2:
            playerTurn = 1

        print("EXITING WITH PLAYER TURN SET TO: " + str(playerTurn))



    print("DONE WITH LOOP")

    # Exit out
    #STAGE_1 = False
