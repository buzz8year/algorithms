# 59067982

# -- ПРИНЦИП РАБОТЫ --
# Реализация с помощью структуры данных "стек".
# Все добавляемые в очередь элементы добавляются в голову стека.
# Все извлекаемые из очереди элементы извлекаются также из головы стека.
# Голова стека движется слева-направо вместе с крайним добавляемым элементом.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Из описания алгоритма следует, что чем позже элемент добавился в очередь,
# тем раньше он будет из неё извлечён, что и требуется по условию задачи.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Добавление в очередь стоит O(1).
# Извлечение из очереди стоит в лучшем случае O(1).
# Временаая сложность алгоритма O(1)
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Стек, содержащий k элементов, занимает O(k) памяти.
# Поэтому и моя очередь будет потреблять O(n) памяти.


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
