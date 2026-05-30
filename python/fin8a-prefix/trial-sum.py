def do_sum(data):
    return sum(data)


if __name__ == '__main__':
    data = []
    for _ in range(105):
        data.append(float(input()))

    print(do_sum(data))
