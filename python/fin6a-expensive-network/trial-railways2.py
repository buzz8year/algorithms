class Graph:
    def __init__(self, n):
        self.graph = dict()
        self.colors = dict()
        self.visited = dict()
        for i in range(1, n + 1):
            self.visited[i] = False
            self.colors[i] = 'white'
            self.graph[i] = []

    def insert(self, u, v, type_b=True):
        if type_b:
            self.graph[u].append(v)
        else:
            self.graph[v].append(u)

    def dfs(self, v):
        # self.visited[v] = True
        self.colors[v] = 'gray'
        for next_v in self.graph[v]:
            # if not self.visited[next_v]:
            if self.colors[next_v] == 'white':
                return self.dfs(next_v)
            # else: return 'NO'
        self.colors[v] = 'black'
        return 'YES'


if __name__ == '__main__':
    n = int(input())
    g = Graph(n)

    for k in range(1, n):
        row = input()
        for i in range(len(row)):
            g.insert(k, k + i + 1, row[i] == 'B')

    if g.dfs(1):
        print('YES')
    else:
        print('NO')
