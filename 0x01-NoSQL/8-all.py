#!/usr/bin/env python3
"""
This module provides a function that lists all documents
in a mongo db collection.
"""


def list_all(mongo_collection):
    """Lists alll documents in a collectrion
    Args:
        mongo_collection: the pymongo collection object

    Returns:
        an empty list if no document in the collection
        the list of documents
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
