# -- PROBLEM STATEMENT --
# Given a binary search tree that stores keys.
# Find the vertex with the given key and remove it from the tree so that the tree remains a valid binary search tree.
# If the key is not in the tree, do not modify the tree.
# The root of the tree and the key to be deleted are passed as input to your function.
# The function should return the root of the modified tree.
# The complexity of node deletion should be O(h), where h is the height of the tree.
# You can’t create new peaks (even if you suddenly really feel like it).

# -- INPUT FORMAT --
# The tree keys are natural numbers not exceeding 10^9.

# -- SOLUTION OPERATING PRINCIPLE --
# We look for the node that needs to be deleted. We define the base cases.
# We look for the node that will be used as a replacement. We pass the children of the replacement node to its parent.
# We perform the replacement.

# -- SOLUTION TIME COMPLEXITY --
# The time complexity of the deletion operation in the worst case will be O(h), where h is the height of the tree.

# -- SOLUTION SPACE COMPLEXITY --
# O(h) additional memory will be required, where h is the height of the tree.


# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.value = value
#         self.right = right
#         self.left = left

def remove(node, val):
    if node is None:
        return None

    if val < node.value:
        node.left = remove(node.left, val)
        return node
    elif val > node.value:
        node.right = remove(node.right, val)
        return node

    if node.left is None and node.right is None:
        return None

    if node.left is None:
        return node.right
    elif node.right is None:
        return node.left

    swap_parent = node
    swap = node.right

    while swap.left is not None:
        swap_parent = swap
        swap = swap.left

    if swap_parent != node:
        swap_parent.left = swap.right
    else:
        swap_parent.right = swap.right

    node.value = swap.value
    return node
