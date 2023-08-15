#!/usr/bin/env python3
"""
List all documents from mongo collection module
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection:
    """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)

    return documents
