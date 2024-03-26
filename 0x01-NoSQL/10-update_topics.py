#!/usr/bin/env python3

"""
a script that updates the values of a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    A function that adds new field to an already exiting collection
    Argument:
            mongo_collection(mongo Object): a mongo object
            name(string): name of the school
            topics(list): an array of topics
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
