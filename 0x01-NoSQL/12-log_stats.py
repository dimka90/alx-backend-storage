#!/usr/bin/env python3

"""
A script that read some data from a collection
"""


import pymongo


def log_nginx_stats():
    """
    A function that prints the values of
    various form methods for nginx
    """
    # connecting to the database
    db_connection = pymongo.MongoClient("mongodb://localhost/27017")
    # select the database
    database = db_connection["logs"]
    # select the connection collection
    collection = database["nginx"]
    # Http methods
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # printing the value of match
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for http_action in method:
        # printing the the match and total count
        count = collection.count_documents({"method": http_action})
        print("\t{}: {}".format(http_action, count))
        count_status = collection.count_documents({"method": "GET",
                                                  "path": "/status"})
    print(f"{count_status} status check")


if 'name' == __main__':
    log_nginx_stats()
