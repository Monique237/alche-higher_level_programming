#!/usr/bin/python3
"""Define a custom list class with sorted printing."""


class MyList(list):
    """Represent a list with a method for sorted printing."""

    def print_sorted(self):
        """Print the elements of the list in ascending order."""
        print(sorted(self))
