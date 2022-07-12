#!/usr/bin/python
import json


"""Module that handles JSON"""


def to_json_string(my_obj):
    """Serializes an object into JSON"""
    return json.dumps(my_obj)
