#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """ 
    lis all documents
    """

    documents = mongo_collection.find({})
    return list(documents)
