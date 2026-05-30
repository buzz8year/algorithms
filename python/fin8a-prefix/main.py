# 67562918

# -- ПРИНЦИП РАБОТЫ --
# Распаковываем строки. Находим длину самой короткой из них. Посимвольно сравниваем строки слева направо,
# инкрементируя индекс. Наткнувшись на первое различие прерываем цикл и запоминаем индекс.
# Общим префиксом будет подстрока от левого начала до значения индекса.

# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(n^2 * L) времени, где n — количество строк, а L - длина самой длинной из распакованны строк.

# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# В худшем случае потребуется O(n*L) дополнительной памяти, где n — количество строк,
# а L - длина самой длинной из распакованны строк.


def unpack(row):
    while True:
        rght = row.find(']')
        if rght == -1:
            return row

        left = row.rfind('[', 0, rght)
        n = int(row[left-1])

        row = row[:left-1] + row[left+1:rght] * n + row[rght+1:]


def longest_prefix(rows):
    for i, row in enumerate(rows):
        rows[i] = unpack(row)

    min_len = min(len(row) for row in rows)

    index = 0
    while True:
        if index >= min_len:
            break

        char = rows[0][index]

        if all(rows[j][index] == char for j in range(1, len(rows))):
            index += 1
        else: break

    return rows[0][:index]


if __name__ == '__main__':
    n = int(input())

    rows = []
    for _ in range(n):
        rows.append(input())

    print(longest_prefix(rows))
