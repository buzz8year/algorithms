class Stack:
    def __init__(self, n):
        self.items = [None] * n
        self.size = 0
        self.head = 0

    def push(self, item):
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


class Graph:
    def __init__(self, n, m):
        self.stack = Stack(m + 1)
        self.graph = {}
        self.visited = {}
        for i in range(1, n + 1):
            self.visited[i] = False
            self.graph[i] = []

    def insert(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v):
        self.stack.push(v)

        while self.stack.size > 0:
            v_from = self.stack.pop()
            if not self.visited[v_from]:
                print(v_from, end=' ')
                self.visited[v_from] = True

            for next_v in sorted(self.graph[v_from], reverse=True):
                if not self.visited[next_v]:
                    self.stack.push(next_v)


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    g = Graph(n, m)

    for k in range(m):
        start, end = (int(i) for i in input().split())
        g.insert(start, end)

    v = int(input())

    g.dfs(v)
