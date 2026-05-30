def unfold(s):
    while True:
        i_close = s.find(']')
        if i_close == -1:
            return s
        i_open = s.rfind('[', 0, i_close)
        n = int(s[i_open-1])

        s = s[:i_open-1] + s[i_open+1:i_close] * n + s[i_close+1:]


def longest_prefix(n, arr):
    for i, s in enumerate(arr):
        arr[i] = unfold(s)

    min_len = min(len(s) for s in arr)

    index = 0
    while True:
        if index >= min_len:
            break
        c = arr[0][index]
        if all(arr[j][index] == c for j in range(1, len(arr))):
            index += 1
        else:
            break
    return arr[0][:index]


# if __name__ == '__main__':
n = int(input())

data = []
for i in range(n):
    data.append(input())

print(longest_prefix(n, data))
