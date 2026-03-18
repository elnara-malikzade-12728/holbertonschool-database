#!/usr/bin/env python3
"""
This module has a Cache class with __init__ method and a private variable 
"""
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    A class with __init__ method and a private variable
    """
    def __init__(self) -> None:
        """
        Method that initializes redis instance and flushes the db
        """
        import redis
        
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Metod that takes uuid data type and returns str
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[int, bytes, float, str, None]:
        data = self._redis.get(key)
        if key is not None and fn is not None:
            return fn(data) 
        return data
