#!/usr/bin/python3

"""
read file
"""
import json


def load_from_json_file(filename):
    """
    create an object
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
