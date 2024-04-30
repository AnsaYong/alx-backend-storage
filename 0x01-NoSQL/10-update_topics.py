#!/usr/bin/env python3
"""
This module provides a function that changes all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    Args:
        mongo_collection: the pymongo collection object
        name (str): the school name to update
        topics (list of str): the list of topics approached in the school

    Returns:
        The number of documents updated
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
