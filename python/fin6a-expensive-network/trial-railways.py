adjacency = dict()

n = int(input())
for i in range(1, n):
    adjacency[i] = input()


def dfs(start, v, v_prev, visited, road_type):
    if v in visited:
        return

    visited.add(v)

    if v_prev:
        e_type = adjacency[v_prev][v - v_prev - 1]
        if not road_type:
            road_type = e_type
        elif e_type != road_type:
            return
        elif e_type != adjacency[start][v - start - 1]:
            print('NO')
            exit()

    for i in range(v + 1, n + 1):
        if i not in visited:
            dfs(start, i, v, visited, road_type)


res = 'FAIL'
for start in range(1, n - 1):
    visited = set()
    road_type = None
    v_prev = 0

    res = dfs(start, start, v_prev, visited, road_type)

print(res)
