#!/usr/bin/python3
"""locked boxes"""

def canUnlockAll(boxes):
    """lockedbox algorithm
    to identify if all boxes can be opened
    :param boxes: list of list
    :return: booleans
    """
    if boxes is None:
        return False
    
    all_boxes = []
    keys = boxes[0]
    not_opened = []
    for i in range(1, len(boxes) - 1):
        all_boxes.append(i)
        if i in keys:
            for j in boxes[i]:
                if j not in keys:
                    keys.append(j)
        else:
            not_opened.append(i)
    for i in not_opened:
        for j in boxes[i]:
            if j not in keys:
                keys.append(j)
    for i in all_boxes:
        if i not in keys:
            return False
    return True
