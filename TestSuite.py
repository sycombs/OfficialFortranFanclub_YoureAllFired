"""@package docstring
Testing suite
I'm just keeping this file around in order to be able to test out whatever
is necessary
"""


from socket import *
import json

# Player stuff
from player import *

testPlayer = Player()
testPlayer.send_player_state()
