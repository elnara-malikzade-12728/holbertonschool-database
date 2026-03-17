#!/usr/bin/env python3
"""
This module has a Cache class with __init__ method and a private variable 
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A class with __init__ method and a private variable
    """
    def __init__(self):
        """
        Method that initializes redis instance and flushes the db
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Metod that takes uuid data type and returns str
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
