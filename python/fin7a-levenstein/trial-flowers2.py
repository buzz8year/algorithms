def get_path(points):
    n = len(points)
    m = len(points[0])
    dp = [[0] * m] * n

    for i in range(n):
        for j in range(m):
            y = n - i - 1
            x = j

            down = 0
            if y + 1 != n:
                down = dp[y + 1][x]

            left = 0
            if x != 0:
                left = dp[y][x - 1]

            dp[y][x] = max(left, down) + points[y][x]

    # print(dp)

    path = ''
    y = 0
    x = m - 1

    while y != n or x != 0:
        if x == 0:
            path += 'U'
            y += 1
            continue

        down = 0
        if y + 1 < n:
            down = dp[y + 1][x]

        left = 0
        if x > 0:
            left = dp[y][x - 1]

        if down > left:
            y += 1
            path += 'U'
        else:
            x -= 1
            path += 'R'

    path = path[:len(path) - 1]

    return path[::-1]


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    points = []
    for _ in range(n):
        points.append([int(i) for i in input()])

    res = get_path(points)
    print(len(res))
    print(res)
