#!/usr/bin/env python3
"""
This module provides a `Cache` class with a `store` method to
store an instance of a Redis client.
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[
                                                    str, bytes, int, float]:
        """
        Gets the value of a key in the cache.

        Parameters
        ----------
        key : str
            The key of the data to retrieve from the cache.

        fn : Callable
            The function to apply to the value retrieved from the cache.

        Returns
        -------
        value : str / bytes / int / float
            The value of the key in the cache.
        """

        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Gets the value of a key in the cache as a string.

        Parameters
        ----------
        key : str
            The key of the data to retrieve from the cache.

        Returns
        -------
        value : str
            The value of the key in the cache as a string.
        """

        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Gets the value of a key in the cache as an integer.

        Parameters
        ----------
        key : str
            The key of the data to retrieve from the cache.

        Returns
        -------
        value : int
            The value of the key in the cache as an integer.
        """

        return self.get(key, fn=lambda x: int(x))
