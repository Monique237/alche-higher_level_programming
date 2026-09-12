#!/usr/bin/python3
"""Provide a function that returns an object's dictionary description."""


def class_to_json(obj):
    """Return the dictionary representation of an object's attributes."""
    return obj.__dict__
