# -- OPERATING PRINCIPLE --
# Implemented using a "stack" data structure.
# All elements added to the queue are placed onto the top of the stack.
# All elements removed from the queue are likewise taken from the top of the stack.
# The top of the stack moves from left to right, following the most recently added element.
#
# -- PROOF OF CORRECTNESS --
# The algorithm's design ensures that the later an element is added to the queue,
# the sooner it is removed—which satisfies the problem's requirements.
#
# -- TIME COMPLEXITY --
# Adding an element to the queue takes O(1) time.
# Removing an element from the queue takes O(1) time in the best case.
# The overall time complexity of the algorithm is O(1).
#
# -- SPACE COMPLEXITY --
# A stack containing k elements occupies O(k) memory.
# Therefore, this queue implementation consumes O(n) memory.

class Stack:
    def __init__(self, n):
        self.items = [None] * n
        self.op_sign = None
        self.result = None
        self.size = 0
        self.head = 0

    def push(self, item):
        self.result = item
        self.items[self.head] = item
        self.head = self.head + 1
        self.size += 1

    def pop(self):
        if len(self.items) > 0:
            h = self.head - 1
            value = self.items[h]
            self.items[h] = None
            self.head -= 1
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


if __name__ == '__main__':
    exp = input().split()
    obj = Stack(len(exp))

    for c in exp:
        if c.lstrip('-').isdigit():
            obj.push(c)

        if obj.size > 1 and c in ['+', '-', '*', '/']:
            obj.op_sign = c
            obj.exec_op()

    print(int(obj.result))
