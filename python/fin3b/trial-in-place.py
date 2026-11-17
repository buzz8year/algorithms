def partition(tuples, left, rght):
    pivot = tuples[rght]
    point = left - 1

    for i in range(left, rght):
        if tuples[i] <= pivot:
            point += 1
            tuples[point], tuples[i] = tuples[i], tuples[point]

    tuples[point + 1], tuples[rght] = tuples[rght], tuples[point + 1]
    return point + 1


def sort_tuples(tuples, left, rght):
    if left < rght:
        i = partition(tuples, left, rght)

        sort_tuples(tuples, left, i - 1)
        sort_tuples(tuples, i + 1, rght)


if __name__ == '__main__':
    n = int(input())

    tuples = []
    for i in range(n):
        inp = input().split()
        tuples.append((-int(inp[1]), int(inp[2]), inp[0]))

    sort_tuples(tuples, 0, n - 1)

    for t in tuples:
        print(t[2])
