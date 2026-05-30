# 67472331

# -- ПРИНЦИП РАБОТЫ --
# Кратчайшее расстояние Левенштейна находится с помощью алгоритма Вагнера-Фишера

# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Потребуется O(m*n) времени, где (m,n) — длины двух строк подлежащих сравнению

# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Потребуется O(m*n) дополнительной памяти, где (m,n) — длины двух строк подлежащих сравнению


def find_distance(a, b):
    if a == b:
        return 0

    matrix = []

    m = len(a) + 1
    n = len(b) + 1

    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)

    for i in range(1, m):
        matrix[i][0] = i
    for j in range(1, n):
        matrix[0][j] = j

    for j in range(1, n):
        for i in range(1, m):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)

    return matrix[m - 1][n - 1]


if __name__ == '__main__':
    a = input()
    b = input()

    print(find_distance(a, b))

