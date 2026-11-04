# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        newNode = ListNode(l1.val + l2.val)
        if l1.next is not None and l2.next is not None:
            self.addTwoNumbers(l1.next, l2.next)


if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(4, n1)
    n3 = ListNode(2, n2)

    k1 = ListNode(4)
    k2 = ListNode(6, k1)
    k3 = ListNode(5, k2)

    sol = Solution()
    sol.addTwoNumbers(n3, k3)
