class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) > 0:
            self.items.append(max(self.items[-1], item))
        else:
            self.items.append(item)

    def pop(self, item=None):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print('error')

    def get_max(self, item=None):
        if len(self.items) > 0:
            print(self.items[-1])
        else:
            print('None')


n = int(input())

obj = Stack()

while n > 0:
    method = input().split()
    arg = None if len(method) < 2 else method[1]

    fun = getattr(obj, method[0])

    fun(arg)

    n -= 1