import random


class Stack:
    def __init__(self, items):
        self.items = items
        self.blocks = []

    def get_parts(self, items, pivot):
        left, center, right = [], [], []

        for i in items:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                center.append(i)
            else:
                right.append(i)

        self.blocks = [left, center, right]
        return left, center, right

    def quicksort(self, items):
        print('items', items, self.blocks)
        if len(items) < 2:
            return items
        else:
            # pivot = random.choice(items)
            pivot = items[0]
            left, center, right = self.get_parts(items, pivot)
            return self.quicksort(left) + center + self.quicksort(right)


if __name__ == '__main__':
    n = input()
    data = input().split()
    s = Stack(data)
    s.quicksort(data)

    print(len(s.blocks))

