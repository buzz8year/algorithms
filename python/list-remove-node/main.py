# Comment it before submitting
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get_node_by_index(node, idx):
    while idx and idx >= 0:
        node = node.next
        idx -= 1

    return node


def remove_node(node, idx):
    if idx == 0:
        node = node.next
        return node

    prev = get_node_by_index(node, idx - 1)
    prev.next = prev.next.next
    return node


def solution(node, idx):
    head = remove_node(node, idx)
    return head


def test():
    # v0 = "node0"
    # v1 = "node1"
    # v2 = "node2"
    # v3 = "node3"
    # v4 = "node4"
    # v5 = "node5"

    # v0 = "nc drokktmo d nhb o rtaahhpm uvgfpqro zinllo qj"
    # v1 = "vzmdumww wyzp fzjxs t qa bvcoqjzs qodkaz gfm shsoy"
    # v2 = "imszpmcyy xwkexdg iepuumu hrtvemtgbj limbi xvtda reg bpdml eqmwqgza"
    # v3 = "cdma qe k yoaq oxvmnyjn zsjbzw w sxisomewjx"
    # v4 = "zcwqolme mmnrbsufr fblnglukzy ac jzrhlj ywqeeniwmp d kwvodbsuxj tc"
    # v5 = "utvgqfqhgo wbua gga i fs oetulstshr df kq jvor ke"

    v0 = "gj hmaw wcqe vbzfp slg"
    v1 = "gjytmyid sm dvxwgybe auyrvenc rjnm lfockfc peyxp"
    v2 = "iyqiebxh gclc"

    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    new_head = solution(node0, 2)

    print_list_head(new_head)


def print_list_head(head):
    if head is not None:
        print(head.value)
    else:
        print('---')

    if head.next is not None:
        print_list_head(head.next)


test()