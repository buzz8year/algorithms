def get_top(values, k):
    if len(values) == 0:
        return {}

    counter = dict()

    for val in values:
        counter[val] = counter.get(val, 0) + 1

    result = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return result[:k]


if __name__ == '__main__':
    n = int(input())
    values = [int(i) for i in input().split()]
    k = int(input())

    # print(values)
    combs = get_top(values, k)
    for i in combs:
        print(i[0], end=' ')
