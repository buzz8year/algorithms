class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()

    def get_last(self):
        return self.items[-1]

    def empty(self):
        if len(self.items) > 0:
            return False
        else:
            return True


def process(str):
    stack = Stack()

    for c in str:
        if c == '(':
            stack.push(')')
        elif c == '[':
            stack.push(']')
        elif c == '{':
            stack.push('}')
        elif stack.empty() or stack.get_last() is not c:
            return False
        else:
            stack.pop()

    return stack.empty()


def is_correct_bracket_seq(str):
    print(process(str))


brs = input()
is_correct_bracket_seq(brs)