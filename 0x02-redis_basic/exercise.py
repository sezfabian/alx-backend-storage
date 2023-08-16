#!/usr/bin/env python3
"""
Writing strings to Redis Module
"""
import redis
import uuid
from typing import Union, Callable

class Cache:
    """
    Create a Cache class
    """
    def __init__(self):
        """
        store an instance of the Redis client as a private variable named _redis
        and flush the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method that takes a data argument and returns a string
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, list]:
        """
        Reading from Redis and recovering original type
        """
        value = self._redis.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)

      def get_str(self, data: bytes) -> str:
        """ 
        Converts byte string to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ 
        Converts byte string to integers
        """
        return int(data)
