#!/usr/bin/python3

def canUnlockAll(boxes):
    """This function determines if all the boxes can be opened."""
    if not boxes or type(boxes) is not list:
        return False

    number_of_boxes = len(boxes)
    opened_boxes = [0]

    for box_index in opened_boxes:
        for key in boxes[box_index]:
            if key < number_of_boxes and key not in opened_boxes:
                opened_boxes.append(key)
    return len(opened_boxes) == number_of_boxes
