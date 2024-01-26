#!/usr/bin/env python3
"""A module with tools for request caching and tracking.
"""
import redis
from requests import get
from functools import wraps
from typing import Callable


r = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """Caches the output of fetched data.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """Returns the cached data if available, otherwise fetches it.
        """
        r.incr(f"count:{url}")
        name: str = method.__qualname__
        if r.get(name) is not None:
            return r.get(name)
        result = method(url)
        r.setex(name, 10, result)
        return r.get(name)
    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """Returns the content of a URL after caching the request's response,
    and tracking the request.
    """
    return get(url).text
