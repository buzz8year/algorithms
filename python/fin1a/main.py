def minimize(items):
    left = populate(items)
    right = populate(items[::-1])

    finals = [min(l, r) for l, r in zip(left, right[::-1])]

    finals = [str(d) for d in finals]

    return " ".join(finals)


def populate(items):
    lefts = n * [0]
    last = -1

    for z in range(0, n):
        if items[z] == '0':
            for i in range(last + 1, z):
                lefts[i] = abs(i - z)

            last = int(z)

    if last < n:
        for i in range(last + 1, n):
            lefts[i] = n

    return lefts


if __name__ == '__main__':
    n = int(input())
    result = minimize(list(input().split()))

    print(result)


