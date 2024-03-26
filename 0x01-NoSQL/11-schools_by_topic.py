#!/usr/bin/env python3

"""
A script that search a topic in a collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools with a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of schools with the specified topic.
    """
    # Find all documents that contain the specified topic
    # in their 'topics' field
    cursor = mongo_collection.find({"topics": topic})

    # Initialize a list to store the schools
    schools = []

    # Iterate over the cursor to extract the schools
    for doc in cursor:
        schools.append(doc)

    return schools
