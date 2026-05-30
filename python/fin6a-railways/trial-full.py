class Graph:
    def __init__(self, n, m):
        self.visited = dict()
        self.graph = dict()

        for i in range(1, n + 1):
            self.visited[i] = False
            self.graph[i] = []

    def insert(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def check_full(self):
        # print(self.graph)
        for i in range(1, len(self.graph)):
            # print(self.graph[i])
            if len(self.graph) - len(self.graph[i]) > 1:
                return False
        return True


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    g = Graph(n, m)

    for k in range(m):
        start, end = (int(i) for i in input().split())
        g.insert(start, end)

    print('YES' if g.check_full() else 'NO')
