#!/usr/bin/env python3
"""
Writing strings to Redis Module
"""
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache class methods to track call count
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wraps called method and adds its call count redis before execution
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ Decorator for Cache class method to track args
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """ Wraps called method and tracks its passed argument by storing
            them to redis
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper

def replay(fn: Callable) -> None:
    """ Check redis for how many times a function was called and display:
            - How many times it was called
            - Function args and output for each call
    """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was called {calls} times:')
    for input, output in zip(inputs, outputs):
        print(f'{fn.__qualname__}(*{input}) -> {output}')

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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method that takes a data argument and returns a string
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
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

