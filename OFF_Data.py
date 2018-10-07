"""@package docstring
Official Fortran Fanclub Data Module

OFF_Data.py will handle all the (de)serialization that's necessary so that any
changes to how we handle data is separated from the network code

Currently only JSON formats are acceptable

See https://docs.python.org/3/library/json.html#json-to-py-table for details
on how the data is being transformmed

I'm sorry that I didn't write this well, you shouldn't need to manually
(de)serialize data! The first extension anyone adds should be to add automatic
message (de)serializatin
"""

import json

def serialize_data(rawData):
    """
    serialize_data() will return a JSON object that represents the raw data
    passed

    *** WARNING: THIS WORKS BEST WHEN rawData IS A DICTIONARY. OTHER FORMATS
    ARE NOT CURRENTLY HANDLED WELL IN THE OFF_Network send_comm() METHOD ***

    Restrictions:
        rawData must be a dictionary, string, or int

    If an exception occurs, return ERROR? False? None? What do I do?
    """

    try:
        jsonData = json.dumps(rawData)
        return jsonData
    except Exception as e:
        print("ERROR: serialize_data")
        print(e)

def deserialize_data(serialData):
    """
    deserialize_data will attempt to unserialize and return data

    Data received should be easily convertable. The following has a table
    with the encode / decode formats for  JSON to Python
    https://docs.python.org/3/library/json.html#json-to-py-table

    Restrictions:
        serialData is currently limited to JSON only

    If an exception occurs, return ERROR? False? None? What do I do?
    """

    try:
        deserialData = json.loads(serialData)
        return deserialData
    except Exception as e:
        print(e)
        return "ERROR"
