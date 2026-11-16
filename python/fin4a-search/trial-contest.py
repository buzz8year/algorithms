def get_max_len(data):
    sum_to_pos = dict()
    max_len = 0
    total = 0

    for i in range(len(data)):
        total += 1 if data[i] > 0 else -1

        if total == 0:
            max_len = i + 1
        elif total in sum_to_pos:
            max_len = max(max_len, i - sum_to_pos[total])
        else:
            sum_to_pos[total] = i

    return max_len


if __name__ == '__main__':
    n = int(input())

    if n == 0:
        print(0)
    else:
        data = [int(i) for i in input().split()]
        print(get_max_len(data))
