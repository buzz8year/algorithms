def get_max_coins(nominals, x):
    dp = [0] * (x + 1)
    current_sum = 1
    while current_sum <= x:
        dp[current_sum] = x
        for nominal in nominals:
            if nominal <= current_sum:
                dp[current_sum] = min(dp[current_sum], dp[current_sum - nominal] + 1)
        current_sum += 1

    if dp[x] == 0: return -1
    else: return dp[x]


if __name__ == '__main__':
    x = int(input())
    k = int(input())
    nominals = [int(i) for i in input().split()]

    print(get_max_coins(nominals, x))
