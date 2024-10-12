#!/usr/bin/python3
""" An Alx interview task on Lockboxes"""
from typing import List


def canUnlockAll(boxes:List[List[int]]) -> bool:
    """ A function that performs the
    locked boxes task"""
    n = len(boxes)
    unlocked = set([0])
    keys = list(boxes[0])


    while keys:
        key = keys.pop()
        if key <= n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == n
