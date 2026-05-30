if __name__ == '__main__':
    n, m = (int(i) for i in input().split())

    matrix = [['0']*n for i in range(n)]

    for k in range(m):
        start, end = (int(i) - 1 for i in input().split())
        matrix[start][end] = '1'

    for row in matrix:
        print(' '.join(row))

