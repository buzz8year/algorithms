def kmp(row):
    pi = [0] * len(row)
    # print(pi)
    for i in range(1, len(row)):
        j = pi[i - 1]
        while j > 0 and row[i] != row[j]:
            j = pi[j - 1]

        if row[i] == row[j]:
            j += 1

        pi[i] = j

    return pi


def get_repeat(row):
    pi = kmp(row)
    return len(row) // (len(row) - pi[-1])


if __name__ == '__main__':
    row = input()
    print(get_repeat(row))
