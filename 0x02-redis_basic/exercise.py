#!/usr/bin/env python3

"""
A Program that instanciate create and a mongDb Instance
"""

import redis
import uuid
from typing import Union, Any, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable] = None) -> any:
        """
        Retrieve data from the cache.

        Args:
            key (str): The key to retrieve data from.
            fn (Callable): A callable to convert the retrieved data.

        Returns:
            Any: The retrieved data.
        """
        value = self._redis.get(key)
        if value:
            if fn is str:
                return self.get_str(value)
            elif fn is int:
                return self.get_int(value)
            elif callable(fn):
                return fn(value)
            else:
                return value
        else:
            return None

    def get_str(self, data: str) -> str:
        """
        Convert bytes data to a string.

        Args:
            data (bytes): The bytes data to convert.

        Returns:
            str: The converted string.
        """

        return data.decode("utf-8")

    def get_int(self, data: int) -> int:
        """
         Convert bytes data to an integer.

        Args:
            data (bytes): The bytes data to convert.

        Returns:
            int: The converted integer.
        """

        return int(data)
