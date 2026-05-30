def is_search(data, start, template):
    shift = template[0] - data[start]
    for j in range(len(template)):
        if data[start + j] != template[j] - shift:
            return False
    return True


def search(data, template):
    result = []
    size = len(data) - len(template) + 1
    for i in range(size):
        if is_search(data, i, template):
            result.append(i + 1)
    return result


if __name__ == '__main__':
    n = int(input())
    data = [int(i) for i in input().split()]

    m = int(input())
    template = [int(i) for i in input().split()]

    for i in search(data, template):
        print(i, end=' ')

