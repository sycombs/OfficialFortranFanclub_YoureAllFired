"""@package docstring
Testing suite

I'm just keeping this file around in order to be able to test out whatever
is necessary
"""


''' TEST '''

''' This will see whether the logic in STAGE_1 of the CoOp_Logic works. At the
end of the test, the player's ID number should be 1
'''
from OFF_Data import *
from OFF_Network import *

from NetPlayer import *

from time import *

print("Test Suite window")

# Create a player
testPlayer = NetPlayer()

testPlayer.playerData['ID'] = 2

pData = json.dumps(testPlayer.get_player_data())


#print(type(pData))
''' serializedPlayerData is currently a string '''
'''
# Serialize the player's data
serializedPlayerData = serialize_data(testPlayer.get_player_data())

#print("serialize_data is of type: " + str(type(serializedPlayerData)))
#print(serializedPlayerData)
'''

while True:

    # Create the socket to send the data
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Send testPlayer 's data and save the response
    responseData = send_comm(pData, clientSocket, SERVER_INFO, True)

    print(responseData.decode())
    if responseData.decode() != "IT'S NOT YOUR TURN YET":
        # Deserialize the data and assign it to the player
        #processedData = deserialize_data(responseData)

        # Print the player's data
        #testPlayer.set_player_data(processedData)
        #testPlayer.set_player_data(responseData)

        print(testPlayer.get_player_data())

        msg = serialize_data("Board, please")
        #print("msg is of type: " + str(type(msg)))

        hopefullyABoard = send_comm(msg, clientSocket, SERVER_INFO, True)
        print(hopefullyABoard)
    else:
        print("It's not my turn :(")

    sleep(1)
