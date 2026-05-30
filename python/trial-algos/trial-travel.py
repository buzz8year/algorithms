def get_max_arr(data):
    if len(data) < 2:
        return [1]

    maxi = 0
    dp = [1] * len(data)

    for i in range(len(data)):
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        maxi = max(maxi, dp[i])

    positions = list()

    for k in reversed(range(len(dp))):
        if maxi == dp[k]:
            positions.append(k + 1)
            maxi -= 1

    return list(reversed(positions))


if __name__ == '__main__':
    n = int(input())
    data = [int(i) for i in input().split()]

    res = get_max_arr(data)
    print(len(res))
    print(' '.join(map(str, res)))
