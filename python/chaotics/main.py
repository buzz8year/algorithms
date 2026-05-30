def read_func():
    n = int(input())
    tmps = [int(i) for i in input().split()]

    chaotics = 0

    if n > 1:
        for i in range(n):
            if i == 0 and tmps[i] > tmps[i+1]:
                chaotics = chaotics + 1

            if i == (n-1) and tmps[i] > tmps[i-1]:
                chaotics = chaotics + 1

            if (i > 0 and i < (n-1)) and tmps[i] > tmps[i+1] and tmps[i] > tmps[i-1]:
                chaotics = chaotics + 1

    if n == 1:
        chaotics = chaotics + 1

    print(chaotics)


read_func()