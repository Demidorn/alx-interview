#!/usr/bin/python3

"""Lockboxes module that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if not boxes:
        return False
    unlocked = set()
    unlocked.add(0)
    keys = [0]
    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key not in unlocked:
                unlocked.add(key)
                keys.append(key)
    return len(unlocked) == len(boxes)
