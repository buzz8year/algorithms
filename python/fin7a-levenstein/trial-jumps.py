def get_jump(n, k):
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        start, end = max(0, i - k), i
        for j in range(start, end):
            dp[i] = (dp[i] + dp[j]) % 1000000007
    return dp[-1]


if __name__ == '__main__':
    n, k = (int(i) for i in input().split())

    print(get_jump(n, k))
