class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class MyQueueSized:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def empty(self):
        return self.queue_size == 0

    def size(self, arg=None):
        print(self.queue_size)

    def put(self, x):
        node = Node(x, None)
        if self.empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.queue_size += 1

    def get(self, arg=None):
        if self.empty():
            print('error')
        else:
            value = self.head.value
            self.head = self.head.next
            self.queue_size -= 1
            print(value)


n = int(input())

que = MyQueueSized()

while n > 0:
    method = input().split()
    arg = None if len(method) < 2 else method[1]

    fun = getattr(que, method[0])

    fun(arg)

    n -= 1
