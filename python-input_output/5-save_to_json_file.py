#!/usr/bin/python3

"""
read file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save object
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
