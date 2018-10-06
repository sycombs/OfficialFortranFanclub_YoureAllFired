from NetPlayer import *
from Board import *

from OFF_Data import *
from OFF_Network import *

# Assume we're using SERVER_INFO for all of these requests
def send_message(message, sourceSocket):
    request = serialize_data({'Message': message})
    response = send_comm(request, sourceSocket, SERVER_INFO)
