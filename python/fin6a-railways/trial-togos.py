def get_distances(n, m):
    dist = [[999999] * m] * n

    for i in range(m):
        from_, to_, weight = [int(i) for i in input().split()]

        dist[from_ - 1][to_ - 1] = min(dist[from_ - 1][to_ - 1], weight)
        dist[to_ - 1][from_ - 1] = min(dist[to_ - 1][from_ - 1], weight)

    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

    return dist


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    print(get_distances(n, m))

