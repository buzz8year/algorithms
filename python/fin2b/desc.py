# -- OPERATING PRINCIPLE --
# I have implemented a queue using two stacks.
# All elements added to the queue are placed into an input stack.
# All elements removed from the queue are taken from an output stack.
#
# If the output stack is empty when an element is to be removed,
# all elements are moved from the input stack to the output stack,
# which effectively reverses their order.
#
# -- PROOF OF CORRECTNESS --
# The algorithm ensures that the earlier an element is added to the queue,
# the earlier it will be removed.
#
# The output stack stores elements in the reverse order of their arrival
# into the input stack.
#
# A stack follows the LIFO (Last-In, First-Out) principle, while a queue follows FIFO (First-In, First-Out).
# A stack inverts the order of elements—the first become the last.
# Since two stacks are used, the order is inverted twice,
# ultimately restoring the elements to their original order.
#
# -- TIME COMPLEXITY --
# Adding an element to the queue takes O(1) time, as pushing onto the input stack is an O(1) operation.
#
# Removing an element from the queue takes O(1) time in the best case—when the output stack is not empty.
#
# In the worst case, removal takes O(n) time, occurring when the output stack is empty
# and all elements must be transferred from the input stack to the output stack.
#
# Considering the average complexity of removing an element from the queue:
# Each element is moved from one stack to the other exactly once. # This means that adding and removing a total of n elements will cost O(n).
# On average, we get O(n) / n ~ O(1) — the amortized complexity.
#
# -- SPACE COMPLEXITY --
# If the queue contains n elements, then the input stack contains n1 elements,
# and the output stack contains n2 elements, where n1 + n2 = n.
#
# A stack containing k elements occupies O(k) memory.
# Therefore, my queue will consume O(n1) + O(n2) = O(n) memory.

class Stack:
    def __init__(self, n):
        self.head = 0
        self.size = 0
        self.items = [None] * n
        self.op_sign = None
        self.result = None

    def push(self, item):
        self.result = item
        self.items[self.head] = item
        self.head = self.head + 1
        self.size += 1

    def pop(self):
        if len(self.items) > 0:
            head = self.head - 1
            value = self.items[head]
            self.items[head] = None
            self.head = head
            self.size -= 1
            return value
        return int()

    def exec_op(self):
        if self.size > 1:
            v2 = int(self.pop())
            v1 = int(self.pop())
            res = None

            if self.op_sign == '+':
                res = v1 + v2
            if self.op_sign == '-':
                res = v1 - v2
            if self.op_sign == '*':
                res = v1 * v2
            if self.op_sign == '/':
                res = v1 // v2

            self.push(res)


exp = input().split()
obj = Stack(len(exp))

for c in exp:
    if c.lstrip('-').isdigit():
        obj.push(c)

    if obj.size > 1 and c in ['+', '-', '*', '/']:
        obj.op_sign = c
        obj.exec_op()

print(int(obj.result))
