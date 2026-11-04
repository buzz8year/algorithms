# -- OPERATING PRINCIPLE --
# A double-ended queue (deque) data structure implemented using a fixed-size array.
# Elements added to the queue are placed at either the head or the tail of the array, depending on the chosen method.
# Elements removed from the queue are likewise taken from either the head or the tail of the array, depending on the chosen method.
# The head of the queue moves from right to left when an element is added to the head.
# The head of the queue moves from left to right when an element is removed from the head.
# The tail of the queue moves from left to right when an element is added to the tail.
# The tail of the queue moves from right to left when an element is removed from the tail.
# The head and tail indices are incremented modulo the array size, creating a circular (wraparound) queue structure.

# -- PROOF OF CORRECTNESS --
# The algorithm's description implies that the later an element is added to the queue,
# the sooner it will be removed from it, which satisfies the problem's requirements.


# -- TIME COMPLEXITY --
# Adding an element to the queue takes O(1) time.
# Removing an element from the queue takes O(1) time in the best case.


# -- SPACE COMPLEXITY --
# An array containing k elements occupies O(k) memory.

class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_front(self, value, arg=None):
        if self.size < self.max_size:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            return 'error'

    def push_back(self, value, arg=None):
        if self.size < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            return 'error'

    def pop_front(self, arg=None):
        if self.size == 0:
            return 'error'
        else:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value

    def pop_back(self, arg=None):
        if self.size == 0:
            return 'error'
        else:
            value = self.queue[self.tail - 1]
            self.queue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return value


if __name__ == '__main__':
    n = int(input())
    max = int(input())

    que = Deque(max)

    while n > 0:
        method = input().split()
        arg = None if len(method) < 2 else method[1]
        fun = getattr(que, method[0])
        res = fun(arg)
        if res is not None:
            print(res)
        n -= 1


