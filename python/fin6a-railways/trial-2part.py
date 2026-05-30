class Graph:
    def __init__(self, n, m):
        self.colors = dict()
        self.visited = dict()
        self.graph = dict()

        for i in range(1, n + 1):
            self.visited[i] = False
            self.graph[i] = []

    def insert(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v_from, color=1):
        self.colors[v_from] = color

        for to in self.graph[v_from]:
            if self.colors[to] == self.colors[v_from]:
                return False

            if self.colors[to] == 0:
                if not self.dfs(to, 3 - color):
                    return False

        return True


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    g = Graph(n, m)

    for k in range(m):
        start, end = (int(i) for i in input().split())
        g.insert(start, end)

    print(g.dfs(1))
