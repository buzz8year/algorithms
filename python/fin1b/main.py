def compare(data):
    cdata = dict()
    for s in data:
        for c in s:
            if c in cdata:
                cdata[c] += 1
            else:
                cdata[c] = 1

    points = 0
    for key in cdata:
        if key.isnumeric() and cdata[key] <= k * 2:
            points += 1

    return points


def pop2do():
    data = []
    for i in range(4):
        data.append(input())

    return compare(data)


if __name__ == '__main__':
    k = int(input())
    print(pop2do())