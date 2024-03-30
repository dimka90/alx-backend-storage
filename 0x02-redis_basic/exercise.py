#!/usr/bin/env python3

"""
A Program that instanciate create and a mongDb Instance
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class to represent a cache using Redis
    """

    def __init__(self):
        """
        Initialize the Cache class.

        Creates a Redis client instance and flushes the Redis database.
        """
        # creating a private vairable that instance the db
        self._redis = redis.Redis()
        # Flush the Redis instance using flushdb
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the cache.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
