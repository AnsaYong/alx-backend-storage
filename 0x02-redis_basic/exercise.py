#!/usr/bin/env python3
"""
This module provides a `Cache` class with a `store` method to
store an instance of a Redis client.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A class to represent a cache.

    ...

    Attributes
    ----------
    _redis : redis.client.Redis
        a Redis client instance

    Methods
    -------
    store(key: str, value: str) -> None
        Store a key-value pair in the cache.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the Cache object.

        Parameters
        ----------
        _redis : redis.client.Redis
            a Redis client instance
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores an instance of a Redit client in the cache.

        Parameters
        ----------
        data : str / bytes / int / float
            The data to store in the cache.

        Returns
        -------
        key : str
            The key of the stored data.
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
