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
            # print('push_front', self.queue, self.head, self.tail)
        else:
            print('error')

    def push_back(self, value, arg=None):
        if self.size < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            # print('push_back', self.queue, self.head, self.tail)
        else:
            print('error')

    def pop_front(self, arg=None):
        if self.size == 0:
            print('error')
        else:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            # print('pop_front', value, self.queue, self.head, self.tail)
            print(value)

    def pop_back(self, arg=None):
        if self.size == 0:
            print('error')
        else:
            value = self.queue[self.tail - 1]
            self.queue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            # print('pop-back', value, self.queue, self.head, self.tail)
            print(value)

    def put(self, x):
        if self.size < self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop(self, arg=None):
        if self.size == 0:
            print(None)
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            print(x)



n = int(input())
max = int(input())

que = Deque(max)

while n > 0:
    method = input().split()
    arg = None if len(method) < 2 else method[1]

    fun = getattr(que, method[0])

    fun(arg)

    n -= 1


