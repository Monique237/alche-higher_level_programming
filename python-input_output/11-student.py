#!/usr/bin/python3
"""Define a Student class with serialization and reload support."""


class Student:
    """Represent a student with public attributes and JSON helpers."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student."""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace student attributes using values from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
