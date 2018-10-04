"""@package docstring
player.py should only store, get, and set relevant player data using standard 
Python data structures, preferrably dictionaries.
"""


''' TODO:
    Rename Player.py to something that doesn't look so much like Play.py and
    doesn't start with a lowercase letter

    Suggestions: NetPlayer.py and NetworkPlayer.py
'''

class Player:
    def __init__(self):
        """
        Doxygen Comments Doxygen Comments Doxygen Comments
        """

        '''
        When creating any sort of player data, look at the following in order
        to make sure it's formatted properly so that we can send it via JSON
        https://docs.python.org/3/library/json.html#json-to-py-table

        (Just make sure to use a dictionary, string, or int and and everything
        will work fine)
        '''
        self.playerData = {'ID': 0, 'msg': 'Just a message', 'win': False}

    def get_player_data(self):
        return self.playerData

    def get_player_ID(self):
        return self.playerData['ID']

    '''
    Here's a quick template to return any data that is added later on

    def get_player_INFO(self):
        return self.playerData['INFO']
    '''

    def send_player_state(self):
        '''
        We can change this to a simple get function and then pass the data
        to the GameClient function that's in charge of sending data
        '''

        # This will serialize the data using the JSON format
        pData = json.dumps(self.playerData)

        # Create a socket
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        # Try sending the data, and if it doesn't work then print some error
        try:
            clientSocket.sendto(pData.encode(), serverInfo)
            response, serverAddress = clientSocket.recvfrom(2048)
        except Exception as e:
            print(e)


        print(type(response))
                #print("I call create stuff here")

            # Make sure to close the socket after we received the data
            #clientSocket.close()
