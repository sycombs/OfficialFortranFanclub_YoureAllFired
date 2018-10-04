"""@package docstring
Official Fortran Fanclub Data Module

OFF_Data.py will handle all the (de)serialization that's necessary so that any
changes to how we handle data is separated from the network code

Currently we use:
    JSON
    Python 3.7 Pickle
"""

import json
import pickle


def pickle_obj(serverSocket, clientAddress, rawData):
    """
    send_obj() sends pickled object data
    """
    try:
        pickleData = pickle.dumps(rawData)
        serverSocket.sendto(pickleData, clientAddress)
    except Exception as e:
        print(e)

def send_json(serverSocket, clientAddress, rawData):
    """
    send_json()
    """
    try:
        jsonData = json.dumps(rawData)
        serverSocket.sendto(jsonData, clientAddress)
    except Exception as e:
        print(e)



''' How do we best structure this?
def serialize_data(rawData):
    Call proper serialization function
'''
