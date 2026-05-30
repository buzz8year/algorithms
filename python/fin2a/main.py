# 59150824


# -- ПРИНЦИП РАБОТЫ --
# Структура данных дек на ограниченном массиве.
# Все добавляемые в очередь элементы добавляются в голову или в хвост массива в зависимости выбранного метода.
# Все извлекаемые из очереди элементы извлекаются также из головы или из хвоста массива в зависимости выбранного метода.
# Голова очереди движется справа-налево вместе с добавленным в голову элементом.
# Голова очереди движется слева-направо вслед за извлеченным из головы элементом.
# Хвост очереди движется слева-направо вместе с добавленным в хвост элементом.
# Хвост очереди движется справа-налево вслед за извлеченным из хвоста элементом.
# Голова и хвост инкрементируются по модулю, чтобы движение очереди было зацикленным.

# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Из описания алгоритма следует, что чем позже элемент добавился в очередь,
# тем раньше он будет из неё извлечён, что и требуется по условию задачи.


# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Добавление в очередь стоит O(1).
# Извлечение из очереди стоит в лучшем случае O(1).


# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Массив, содержащий k элементов, занимает O(k) памяти.


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


