#!/usr/bin/env python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

'''


def canUnlockAll(boxes):
    'determines if all Lockboxes can be opened'
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
