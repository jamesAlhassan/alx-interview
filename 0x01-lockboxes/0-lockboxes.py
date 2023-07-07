#!/usr/bin/env python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """method to determine if all Lockboxes can be opened"""
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        index = unchecked_boxes.pop()
        if not index or index >= n or index < 0:
            continue
        if index not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[index])
            checked_boxes.add(index)
    return n == len(checked_boxes)
