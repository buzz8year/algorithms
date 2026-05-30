def get_count(nominals, total_sum):
    dp = [0] * (total_sum + 1)
    dp[0] = 1

    for nominal in nominals:
        current_sum = nominal
        while current_sum <= total_sum:
            dp[current_sum] += dp[current_sum - nominal]
            current_sum += 1

    return dp[total_sum]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    nominals = [int(i) for i in input().split()]

    print(get_count(nominals, m))
