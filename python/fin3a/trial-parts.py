def get_parts(data):
    parts = 0
    maxi = 0
    for i in range(len(data)):
        maxi = max(maxi, data[i])
        if maxi == i:
            parts += 1

    return parts


if __name__ == '__main__':
    n = int(input())
    data = [int(i) for i in input().split()]

    print(get_parts(data))

