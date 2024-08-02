#!/usr/bin/python3
""" Script module that determines if if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists lockboxes.

    Returns:
    True if all the boxes can be unlocked, False otherwise.
    """

    if not boxes:
        return False

    # Create a list
    visited = [False] * len(boxes)
    visited[0] = True

    # Create a stack to store the boxes
    stack = [0]

    while stack:
        # Checks the top box from the stack
        box = stack.pop()

        # Checks tthrough the box
        for key in boxes[box]:
            # Check if the key is valid and the corresponding box
            # not visited
            if 0 <= key < len(boxes) and not visited[key]:
                # Mark this box as visited
                visited[key] = True
                # Add the box to the stack
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
