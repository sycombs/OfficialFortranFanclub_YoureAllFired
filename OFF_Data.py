"""@package docstring
Official Fortran Fanclub Data Module

OFF_Data.py will handle all the (de)serialization that's necessary so that any
changes to how we handle data is separated from the network code

Currently we use:
    JSON
    Python 3.7 Pickle
"""

import json


'''
    We're going to stick with JSON for testing purposes
'''

def serialize_data(rawData):
    """
    serialize_data() will return a JSON object that represents the raw data
    passed

    Restrictions:
        rawData must be a dictionary, string, or int

    If an exception occurs, return False?
    """

    try:
        jsonData = json.dumps(rawData)
        return jsonData
    except Exception as e:
        print(e)
        return False
