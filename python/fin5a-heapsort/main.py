def heapify(tuples, size, root):
    node = root
    left = (2 * root) + 1
    rght = (2 * root) + 2

    if left < size and tuples[left] > tuples[node]: node = left
    if rght < size and tuples[rght] > tuples[node]: node = rght
    if node != root:
        tuples[root], tuples[node] = tuples[node], tuples[root]
        heapify(tuples, size, node)


def heapsort(tuples):
    size = len(tuples)
    for i in range(size, -1, -1):
        heapify(tuples, size, i)

    for i in range(size - 1, 0, -1):
        tuples[i], tuples[0] = tuples[0], tuples[i]
        heapify(tuples, i, 0)


if __name__ == '__main__':
    n = int(input())

    tuples = []
    for i in range(n):
        inp = input().split()
        tuples.append((-int(inp[1]), int(inp[2]), inp[0]))

    heapsort(tuples)

    for t in tuples:
        print(t[2])
