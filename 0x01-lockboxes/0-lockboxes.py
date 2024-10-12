#!/usr/bin/python3
""" An Alx interview task on Lockboxes"""


def canUnlockAll(boxes):
    """ A function that performs the
    locked boxes task"""
    unlocked = set([0])
    closed = set(boxes[0]).difference(unlocked)

    while len(closed) > 0:
        key = closed.pop()

        if key not in unlocked:
            unlocked.add(key)
            closed = closed.union(boxes[key]).difference(unlocked)
    return len(unlocked) == len(boxes)