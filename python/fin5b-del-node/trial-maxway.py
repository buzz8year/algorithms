# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def get_max_path(root, result):
    if root is None:
        return result

    left_sum = max(get_max_path(root.left, result), 0)
    right_sum = max(get_max_path(root.right, result), 0)

    result = max(result, left_sum + right_sum + root.value)

    print(result)

    return root.value + max(left_sum, right_sum)
    # return result


def solution(root):
    result = 0
    get_max_path(root, result)
    return result


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6
    # print(solution(node5))


if __name__ == '__main__':
    test()
