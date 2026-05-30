# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def insert(root, value):
    if root is None:
        return Node(None, None, value)

    parent = None
    node = root

    while node is not None:
        parent = node
        if value >= parent.value:
            node = parent.right
        else:
            node = parent.left

    if value >= parent.value:
        parent.right = Node(None, None, value)
    else:
        parent.left = Node(None, None, value)

    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6

    # print(new_head.left.value)


if __name__ == '__main__':
    test()
