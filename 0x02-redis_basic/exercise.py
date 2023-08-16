#!/usr/bin/env python3
"""
Writing strings to Redis Module
"""
import redis
import uuid
from typing import Union

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


