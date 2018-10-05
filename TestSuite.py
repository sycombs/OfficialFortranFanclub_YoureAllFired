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

from player import *

# Create a player
testPlayer = Player()

# Serialize the player's data
serializedPlayerData = serialize_data(testPlayer.get_player_data())

# Create the socket to send the data
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Send testPlayer 's data and save the response
responseData = send_comm(serializedPlayerData, clientSocket, SERVER_INFO)

# Deserialize the data and assign it to the player
processedData = deserialize_data(responseData)

# Print the player's data
testPlayer.set_player_data(processedData)

print(testPlayer.get_player_data())
