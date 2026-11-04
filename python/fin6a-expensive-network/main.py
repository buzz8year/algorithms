# -- OPERATING PRINCIPLE --
# A spanning tree (in this case, a maximum spanning tree) is found using Kruskal's algorithm.

# -- TIME COMPLEXITY --
# O(E log E), where E is the number of edges in the graph.

# -- SPACE COMPLEXITY --
# Requires O(E + V) additional memory, where E is the number of edges in the graph and V is the number of vertices.


class Graph:
    def __init__(self, vertice_quantity, edge_quantity):
        self.vertice_quantity = vertice_quantity
        self.edge_quantity = edge_quantity
        self.graph = []

    def insert(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parents, i):
        if parents[i] == i:
            return i
        return self.find(parents, parents[i])

    def merge(self, parents, rank, x, y):
        xroot = self.find(parents, x)
        yroot = self.find(parents, y)

        if rank[xroot] < rank[yroot]:
            parents[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            parents[yroot] = xroot

        else:
            parents[yroot] = xroot
            rank[xroot] += 1

    def find_max_tree(self):
        result = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)

        parents = []
        rank = []

        if len(self.graph) < 1:
            if self.vertice_quantity - self.edge_quantity > 1:
                return 'Oops! I did it again'
            return 0

        if self.edge_quantity - self.vertice_quantity == 1:
            return 'Oops! I did it again'

        for node in range(self.vertice_quantity):
            parents.append(node)
            rank.append(0)

        while e < self.vertice_quantity - 1:
            u, v, w = self.graph[i]
            i = i + 1

            x = self.find(parents, u)
            y = self.find(parents, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.merge(parents, rank, x, y)

        max_weight = 0
        for u, v, w in result:
            max_weight += w

        return max_weight


if __name__ == '__main__':

    n, m = [int(i) for i in input().split()]
    g = Graph(n, m)

    for i in range(m):
        u, v, w = [int(i) for i in input().split()]
        u -= 1
        v -= 1

        g.insert(u, v, w)

    print(g.find_max_tree())
