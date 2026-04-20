#!/usr/bin/env python3
"""
Update school topics
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    - mongo_collection: pymongo collection object
    - name: string, school name to update
    - topics: list of strings, topics approached in the school
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
