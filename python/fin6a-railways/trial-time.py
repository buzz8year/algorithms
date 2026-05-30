# class Time:
#     def __init__(self, in_, out_):
#         self.in_ = in_
#         self.out_ = out_
#

class Graph:
    def __init__(self, n, m):
        self.visited = dict()
        self.graph = dict()
        self.times = dict()

        for i in range(1, n + 1):
            self.visited[i] = False
            self.graph[i] = []
            self.times[i] = [0, 0]

    def insert(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v_from, time):
        self.times[v_from][0] = time
        time += 1

        self.visited[v_from] = True
        for v_to in sorted(self.graph[v_from]):
            if not self.visited[v_to]:
                self.dfs(v_to, time)

        self.times[v_from][1] = time
        time += 1


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    g = Graph(n, m)

    for k in range(m):
        start, end = (int(i) for i in input().split())
        g.insert(start, end)

    print(g.times)
    g.dfs(1, 0)

    print(g.times)
