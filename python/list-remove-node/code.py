def get_node_by_index(node, idx):
    while idx and idx >= 0:
        node = node.next_item
        idx -= 1

    return node


def remove_node(node, idx):
    if idx == 0:
        node = node.next_item
        return node

    prev = get_node_by_index(node, idx - 1)
    prev.next_item = prev.next_item.next_item
    return node


def solution(node, idx):
    head = remove_node(node, idx)
    return head