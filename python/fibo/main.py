def fun(n):
    if n == 1 or n == 0:
        return 1
    return fun(n - 1) + fun(n - 2)


n = int(input())
print(fun(n))