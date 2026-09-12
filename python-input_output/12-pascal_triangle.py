#!/usr/bin/python3
"""Provide a function that generates Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if triangle:
            previous_row = triangle[-1]

            for j in range(1, i):
                value = previous_row[j - 1] + previous_row[j]
                row.append(value)

            row.append(1)

        triangle.append(row)

    return triangle
