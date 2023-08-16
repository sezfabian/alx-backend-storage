#!/usr/bin/env python3
"""
Insert a document in Python module
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the _id of new document inserted in a collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
