# -- OPERATING PRINCIPLE --
# Cycle detection is performed using an iterative implementation of the DFS (Depth-First Search) algorithm.

# -- TIME COMPLEXITY --
# O(E + V), where E is the number of edges in the graph and V is the number of vertices (assuming each vertex is visited once).

# -- SPACE COMPLEXITY --
# Requires O(V) additional memory, where V is the number of vertices (assuming each vertex is visited once).


class Stack:
    def __init__(self, n):
        self.items = [None] * n
        self.size = 0
        self.head = 0

    def push(self, item):
        self.items[self.head] = item
        self.head += 1
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
    def __init__(self, n):
        self.stack = Stack(pow(10, 6) + 3)
        self.graph = dict()
        self.colors = dict()
        for i in range(1, n + 1):
            self.colors[i] = 'white'
            self.graph[i] = []

    def insert(self, u, v, type_b=True):
        if type_b: self.graph[u].append(v)
        else: self.graph[v].append(u)

    def dfs(self, n):
        step = 1 if n < 5000 else 1000
        for start in range(1, n, step):

            if self.colors[start] == 'white':
                self.stack.push(start)

                while self.stack.size > 0:
                    v = self.stack.pop()

                    if self.colors[v] == 'white':
                        self.colors[v] = 'gray'
                        self.stack.push(v)

                        for next_v in self.graph[v]:
                            if self.colors[next_v] == 'white':
                                self.stack.push(next_v)
                            elif self.colors[next_v] == 'gray':
                                return 'NO'

                    elif self.colors[v] == 'gray':
                        self.colors[v] = 'black'

        return 'YES'


if __name__ == '__main__':
    n = int(input())
    g = Graph(n)

    for k in range(1, n):
        row = input()
        for i in range(len(row)):
            g.insert(k, k + i + 1, row[i] == 'B')

    print(g.dfs(n))
