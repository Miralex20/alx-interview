#!/bin/usr/python3
""" Returns a list of lists of integers representing the pascal triangle """


def pascal_triangle(n):
    """Generates pascal triangle up to row n."""

    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif 1 > 0 and j > 0:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
