# Comment it before submitting
class Node:
    def __init__(self, name, value, left=None, right=None):
        self.name = name
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    return find_next(root, root.value)


def find_next(node, max_val):

    if node.value > max_val:
        max_val = node.value

    if node.left is not None:
        max_val = find_next(node.left, max_val)

    if node.right is not None:
        max_val = find_next(node.right, max_val)

    return max_val


def test():
    node9 = Node('node9', 111, None, None)
    node8 = Node('node8', 0, None, node9)
    node7 = Node('node7', 111, None, None)
    node6 = Node('node6', 0, None, None)
    node5 = Node('node5', 0, None, None)
    node4 = Node('node4', 3, node7, node8)
    node3 = Node('node3', 3, node5, node6)
    node2 = Node('node2', 2, None, node4)
    node1 = Node('node1', 2, node3, None)
    node0 = Node('node0', 0, node1, node2)

    print('fin', solution(node0))
    # assert solution(node4) == 3


if __name__ == '__main__':
    test()
