class Deque:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, value):
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop(self):
        value = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


class Graph:
    def __init__(self, n, m):
        self.q = Deque(m + 1)
        self.graph = {}
        self.visited = {}
        for i in range(1, n + 1):
            self.visited[i] = False
            self.graph[i] = []

    def insert(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v):
        self.q.push(v)
        self.visited[v] = True

        # print(self.q.que)

        while self.q.size > 0:
            v_from = self.q.pop()
            print(v_from, end=' ')

            for next_v in sorted(self.graph[v_from]):
                if not self.visited[next_v]:
                    self.q.push(next_v)
                    self.visited[next_v] = True


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    g = Graph(n, m)

    for k in range(m):
        start, end = (int(i) for i in input().split())
        g.insert(start, end)

    v = int(input())

    g.dfs(v)
