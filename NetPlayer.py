"""@package docstring
player.py should only store, get, and set relevant player data using standard
Python data structures, preferrably dictionaries.
"""


''' TODO:
    Rename Player.py to something that doesn't look so much like Play.py and
    doesn't start with a lowercase letter

    Suggestions: NetPlayer.py and NetworkPlayer.py
'''

class NetPlayer:
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


    ''' GET FUNCTION
        We only need one function right now since all player data is in a
        single dictionary, but here's a quick template to return any data that
        is added later on

        def get_player_INFO(self, dictID):
            return self.playerINFO[dictID]
    '''

    def get_player_data(self, dictKey = None):
        # If no value is passed, return the entire playerData structure
        if dictKey == None:
            return self.playerData
        else:
            return self.playerData[dictKey]

    ''' SET FUNCTION
        We only need one function right now since all player data is in a
        single dictionary, but here's a quick template to set any data that is
        added later on

        def set_player_INFO(self, newValue, dictKey = None):
            self.playerINFO[dictKey] = newValue
    '''

    def set_player_data(self, newValue, dictKey = None):
        if dictKey == None:
            self.playerData = newValue
        else:
            self.playerData[dictKey] = newValue
