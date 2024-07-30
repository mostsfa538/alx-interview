#!/usr/bin/python3
"""..."""


def canUnlockAll(boxes):
    """..."""

    n = len(boxes)
    opened_boxes = set()
    opened_boxes.add(0)

    stack = [0]

    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == n
