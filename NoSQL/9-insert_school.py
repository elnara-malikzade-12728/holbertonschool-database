#!/usr/bin/env python3
"""
a Python function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    a Python function that inserts a new document
    in a collection based on kwargs and returns _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
