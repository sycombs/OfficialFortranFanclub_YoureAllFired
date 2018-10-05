"""@package docstring
GameClient.py deals with client specific functionality such as:
    Update player data
    Provide an interface for network communication
    And... other stuff
"""

# By importing OFF_Network we should have access to all of the server
import OFF_Network


''' Do we even need a separate receive_data() function? Currently all it does is
just pings the server with 'hi' and then waits for a response. That's...
pointless since the send_comm() function can be made to do that easily

This will only be useful if we have it wait for data in a drastically different
way?

Instead we could just constantly ping the server with an update request. Just
send it the string 'Update please' or some other nonsense and wait for a
response
'''

def receive_data():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto("hi".encode(), serverInfo)
    serData, serverAddress = clientSocket.recvfrom(2048)

    return serData

# Connect to the server
# Once connected, check to see what the server wants from us
