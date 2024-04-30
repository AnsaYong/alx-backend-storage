#!/usr/bin/env python3
"""This module provides a function that inserts a new document
in a collection in a MongoDB database based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The collection to insert the document into.
        kwargs: The document to insert.

    Returns:
        The new _id of the new document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
