#!/bin/usr/python3
""" Returns a list of lists of integers representing the pascal triangle """


def pascal_triangle(n):
    """Generates pascal triangle up to row n."""
    triangle = []

    if n > 0:
        for i in range(1, n+1):
            row = []
            first = 1
            for j in range(1, i + 1):
                row.append(first)
                first = first * (i-j) // j
            triangle.append(row)
        return triangle
