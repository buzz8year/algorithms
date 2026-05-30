from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def print_range(root, l, r):
    if root is None:
        return

    if root.value < l:
        print_range(root.right, l, r)
    elif root.value > r:
        print_range(root.left, l, r)
    else:
        print_range(root.left, l, r)
        print(root.value)
        print_range(root.right, l, r)


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6
