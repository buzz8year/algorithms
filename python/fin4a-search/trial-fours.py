def get_sum(data, target):
    result = []
    sum_pair = dict()

    if len(data) < 4:
        return result

    for i in range(1, len(data)):
        for j in range(i + 1, len(data)):
            summ = target - data[i] - data[j]
            if summ in sum_pair:
                lhs, rhs = sum_pair[summ]
                result.append([data[i], data[j], lhs, rhs])

        for j in range(i):
            summ = data[i] + data[j]
            sum_pair[summ] = (data[i], data[j])

    return result


if __name__ == '__main__':
    n = int(input())
    s = int(input())

    data = [int(i) for i in input().split()]

    print(get_sum(data, s))
