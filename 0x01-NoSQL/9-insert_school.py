#!/usr/bin/env python3

"""
A script that store collection and return the id of
the collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that returns the id of a created collection
    Argument:
            mongo_collection: a collection of object
            Kwargs: A vairable number of arguments
    Return:
            The id of the newly created object
    """
    result = mongo_collection.insert_one(kwargs)
    # obtaining the id
    result_id = result.inserted_id

    return result_id
