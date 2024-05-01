#!/usr/bin/env python3
"""
This module provides a function that uses the `requests` module
to obtain the HTML of a particular URL and returns it."""
import requests
import redis
import time


# Connect to Redis
redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL.

    Parameters
    ----------
    url : str
        The URL to get the HTML content from.

    Returns
    -------
    str
        The HTML content of the URL.
    """

    # Track the access count for the URL
    access_count_key = f"count:{url}"
    access_count = redis_client.incr(access_count_key)

    # Count the result with an expiration time of 10 seconds
    cache_key = f"cache:{url}"
    cached_content = redis_client.get(cache_key)
    if cached_content:
        return cached_content.decode("utf-8")

    # Fetch the HTML content
    response = requests.get(url)
    html = response.text

    # Store the HTML content in the cache
    redis_client.setex(cache_key, 10, html)

    return html
