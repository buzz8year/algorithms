def fun(n, k):
    lhs = 1
    rhs = 1
    while n > 0:
        tmp = lhs
        lhs = rhs
        rhs = (rhs + tmp) % pow(10, k)
        n -= 1

    return lhs


n, k = input().split()
print(fun(int(n), int(k)))