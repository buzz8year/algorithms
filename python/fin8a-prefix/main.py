# -- OPERATING PRINCIPLE --
# Unpack the strings. Determine the length of the shortest one. Compare the strings character by character from left to right,
# incrementing an index. Upon encountering the first difference, terminate the loop and record the index.
# The common prefix is ​​the substring extending from the beginning to that index.

# -- TIME COMPLEXITY --
# O(n^2 * L) time, where n is the number of strings and L is the length of the longest unpacked string.

# -- SPACE COMPLEXITY --
# In the worst case, O(n * L) additional memory is required, where n is the number of strings
# and L is the length of the longest unpacked string.


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
