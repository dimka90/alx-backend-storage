#!/usr/bin/env python3

"""
A program that takes in a collection of documents
and return the each documents
"""
import pymongo


def list_all(mongo_collection) -> list:
    """
    A function that returns a list of all documents in
    a list
    Argument:
            mongo_collection: collection of documents
    """
    # Connect to the MongoDb

    all_documents = mongo_collection.find({})
    # convert cursor to a list

    document_list = list(all_documents)

    return document_list
