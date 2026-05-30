# from node import Node

# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def remove(root, val):
    if root is None:
        return None

    del_parent, del_child, to_insert = None, None, None
    to_delete = root
    is_left = False

    while to_delete is not None:
        if to_delete.value == val:
            break

        del_parent = to_delete
        if val >= del_parent.value:
            to_delete = del_parent.right
            is_left = False
        else:
            to_delete = del_parent.left
            is_left = True

    if to_delete is not None:
        if to_delete.left is not None:
            del_child = to_delete.left
        elif to_delete.right is not None:
            del_child = to_delete.right

        if del_child is not None:
            to_insert = find_substitute(del_child)

            if to_delete.right is not None and to_delete.right is not to_insert:
                to_insert.right = to_delete.right
            if to_delete.left is not None and to_delete.left is not to_insert:
                to_insert.left = to_delete.left

    if del_parent is None:
        root = to_insert
    elif is_left:
        del_parent.left = to_insert
    else:
        del_parent.right = to_insert

    return root


def find_substitute(root):
    substitute = root
    parent = None

    while substitute.right is not None:
        parent = substitute
        substitute = substitute.right

    if parent is not None:
        parent.right = substitute.left

    return substitute


def list_tree(root):
    return pop_list(root, [])


def pop_list(node, data):
    l = node.left.value if node.left else None
    r = node.right.value if node.right else None

    data.append((node.value, l, r))

    if node.left is not None:
        pop_list(node.left, data)
    if node.right is not None:
        pop_list(node.right, data)

    return data


def test():
    # node10 = Node(None, None, 867)
    # node9 = Node(None, None, 701)
    # node8 = Node(node9, None, 763)
    # node7 = Node(node8, node10, 858)
    # node6 = Node(None, None, 442)
    # node5 = Node(None, node6, 302)
    # node4 = Node(None, None, 130)
    # node3 = Node(node4, node5, 220)
    # node2 = Node(node3, node7, 624)
    # node1 = Node(None, node2, 31)
    # root = remove(node1, 701)

    node10 = Node(None, None, 840)
    node9 = Node(None, None, 708)
    node8 = Node(None, None, 609)
    node7 = Node(None, node8, 568)
    node6 = Node(node7, None, 626)
    node5 = Node(node6, node9, 649)
    node4 = Node(node5, node10, 818)
    node3 = Node(None, None, 270)
    node2 = Node(node3, None, 355)
    node1 = Node(node2, node4, 460)
    root = remove(node1, 568)

    # node7 = Node(None, None, 7)
    # node6 = Node(None, None, 5)
    # node5 = Node(None, None, 3)
    # node4 = Node(None, None, 1)
    # node3 = Node(node6, node7, 6)
    # node2 = Node(node4, node5, 2)
    # node1 = Node(node2, node3, 4)
    # root = remove(node1, 4)

    # node3 = Node(None, None, 7)
    # node2 = Node(None, node3, 3)
    # node1 = Node(node2, None, 10)
    # root = remove(node1, 10)

    # assert root.value == 668
    # assert root.right is node5
    # assert root.right.value == 702

    print('fin/z', list_tree(root))


if __name__ == '__main__':
    test()
