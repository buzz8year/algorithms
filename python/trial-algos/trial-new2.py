def get_max_subarray(a, b):
    dp = [[0] * (len(b) + 1)] * (len(a) + 1)

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    res_a = list()
    res_b = list()

    a_pos = len(a)
    b_pos = len(b)

    while a_pos > 0 and b_pos > 0:
        if a[a_pos - 1] == b[b_pos - 1]:
            a_pos -= 1
            b_pos -= 1

            res_a.append(a_pos)
            res_b.append(b_pos)
        else:
            if dp[a_pos - 1][b_pos] > dp[a_pos][b_pos - 1]:
                a_pos -= 1
            else: b_pos -= 1

        print(a_pos, b_pos)

    print(res_a, res_b)
    return list(reversed(res_a)), list(reversed(res_b))


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]

    m = int(input())
    b = [int(i) for i in input().split()]

    print(get_max_subarray(a, b))
