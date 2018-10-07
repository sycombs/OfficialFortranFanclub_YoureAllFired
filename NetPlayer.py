"""@package docstring
NetPlayer.py should only store, get, and set relevant player data using standard
Python data structures, preferrably dictionaries.

NetPlayer is only neccessary when playing online and information has to be sent
or received by a client/server
"""

class NetPlayer:
    def __init__(self):
        """
        __init__ just sets up sets up a basic dictionary with some of the
        information necessary to play a network game

        (Note: We can remove win and just use msg to relay that information,
        but there's no real reason to do so since it's such a small amount of
        extra data)
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
        """
        get_player_data() has two cases
            Case 1: If dictKey is empty, return the entire playerData dictionary
            Case 2: If dictKey is not empty, return only the specified entry
        """
        # If no value is passed, return the entire playerData structure
        return self.playerData
        #if dictKey == None:
            #return self.playerData
        #else:
            #return self.playerData[dictKey]

    ''' SET FUNCTION
        We only need one function right now since all player data is in a
        single dictionary, but here's a quick template to set any data that is
        added later on

        def set_player_INFO(self, newValue, dictKey = None):
            self.playerINFO[dictKey] = newValue
    '''

    def set_player_data(self, newValue, dictKey = None):
        """
        set_player_data() has two cases
            Case 1: If dictKey is empty, update the entire playerData dictionary
            Case 2: If dictKey is not empty, update only the specified entry
        """
        if dictKey == None:
            self.playerData = newValue
        else:
            self.playerData[dictKey] = newValue
