def get_max_weight(weights, capacity):
    dp = [0] * (capacity + 1)
    dp[0] = 1
    maxi = 0
    for weight in weights:
        i = capacity
        while i >= weight:
            if dp[i - weight] == 1:
                dp[i] = 1
                maxi = max(maxi, i)
            i -= 1

    return maxi


if __name__ == '__main__':
    n, capacity = [int(i) for i in input().split()]
    weights = [int(i) for i in input().split()]

    print(get_max_weight(weights, capacity))
