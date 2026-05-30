def fib(n):
    lhs = 1
    rhs = 1
    for i in range(n):
        lhs, rhs = rhs, lhs
        rhs = (lhs + rhs) % (pow(10, 9) + 7)
    return lhs


if __name__ == '__main__':
    n = int(input())

    print(fib(n))
