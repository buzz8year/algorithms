def get_max_points(points):
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

    return dp[0][m - 1]


if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    items = []
    for _ in range(n):
        items.append([int(i) for i in input()])

    print(get_max_points(items))
