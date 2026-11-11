# -- PROBLEM --
# You are given strings in a packed format. Let us define a "packed string" (PS) recursively:
# a string consisting solely of lowercase English letters is a PS. If A and B are valid PSs,
# then AB is also a PS. If A is a PS and n is a single-digit natural number, then n[A] is also a PS;
# here, the notation n[A] means that, upon unpacking, the string A is repeated n times consecutively.
# Find the longest common prefix of the unpacked strings and output it (in its unpacked form).

# -- INPUT FORMAT --
# The first line contains an integer n(1≤n≤1000) — the number of strings.
# This is followed by n lines, each containing a packed string.
# It is guaranteed that these strings are valid, meaning they satisfy the specified recursive definition.
# The length of the strings after unpacking does not exceed 10^5.

# -- Example 1 --
# INPUT:
# 3
# 2[a]2[ab]
# 3[a]2[r2[t]]
# a2[aa3[b]]
# OUTPUT:
# aaa

# -- Example 2 --
# INPUT:
# 3
# abacabaca
# 2[abac]a
# 3[aba]
# OUTPUT:
# aba

# -- NOTES --
# Addition is understood as the concatenation of two strings.
# Multiplying a string by a number means repeating the string that number of times.
# Let f be a function that can take a structured string (SS) and unpack it.
# If an SS D is of the form D=AB, where A and B are also SSs, then f(D)=f(A)+f(B). If D=n[A], then f(D)=f(A)×n.

# -- SOLUTION OPERATING PRINCIPLE --
# Unpack the strings. Determine the length of the shortest one. Compare the strings character by character from left to right,
# incrementing an index. Upon encountering the first difference, terminate the loop and record the index.
# The common prefix is ​​the substring extending from the beginning to that index.

# -- SOLUTION TIME COMPLEXITY --
# O(n^2 * L) time, where n is the number of strings and L is the length of the longest unpacked string.

# -- SOLUTION SPACE COMPLEXITY --
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
