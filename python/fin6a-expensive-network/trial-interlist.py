if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    v = []
    for i in range(1, n + 1):
        v.append([])

    for i in range(m):
        start, end = input().split()
        start = int(start) - 1
        v[start].append(end)

    for v_tos in v:
        line = str(len(v_tos)) + ' '
        line += ' '.join(v_tos)
        print(line)




