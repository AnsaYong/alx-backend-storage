#!/usr/bin/env python3
"""
This module provides a `Cache` class with a `store` method to
store an instance of a Redis client.
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


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

    def count_calls(method: Callable) -> Callable:
        """
        Counts the number of times a method is called.

        Parameters
        ----------
        method : Callable
            The method to count the number of calls.

        Returns
        -------
        wrapper : Callable
            The wrapper function that counts the number of calls.
        """

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            The wrapper function that counts the number of calls.

            Parameters
            ----------
            self : Cache
                The Cache object.

            Returns
            -------
            method : Callable
                The method to count the number of calls.
            """

            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        Stores the history of inputs and outputs for a method.

        Parameters
        ----------
        method : Callable
            The method to store the history of inputs and outputs.

        Returns
        -------
        wrapper : Callable
            The wrapper function that stores the history of inputs and outputs.
        """

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            The wrapper function that stores the history of inputs and outputs.

            Parameters
            ----------
            self : Cache
                The Cache object.

            Returns
            -------
            method : Callable
                The method to store the history of inputs and outputs.
            """

            key = method.__qualname__
            self._redis.rpush(f"{key}:inputs", str(args))
            value = method(self, *args, **kwargs)
            self._redis.rpush(f"{key}:outputs", str(value))
            return value
        return wrapper

    @staticmethod
    def replay(method: Callable) -> None:
        """
        Replays the history of inputs/outputs of a method.

        Parameters
        ----------
        method : Callable
            The method to replay the history of inputs/outputs.
        """

        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)
        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for i, o in zip(inputs, outputs):
            print(
                f"{method.__qualname__}("
                f"*{i.decode('utf-8').split(', ')}"
                f") -> {o.decode('utf-8')}"
            )

    @count_calls
    @call_history
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
