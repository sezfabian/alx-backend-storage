#!/usr/bin/env python3
"""
Find by topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that finds all documents in a collection
    that have a specific topic
    """
    return mongo_collection.find({"topics": topic})
