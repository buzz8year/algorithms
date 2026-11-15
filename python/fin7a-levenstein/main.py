# -- PROBLEM STATEMENT --
# The Levenshtein distance between two strings, s and t, is the number of atomic operations
# required to transform one string into the other. Atomic operations are defined as follows:
# deleting a character, inserting a character, or substituting one character for another.
# Find the Levenshtein distance for the given pair of strings.
# Output a single number — the distance between the strings.

# -- INPUT FORMAT --
# The first line contains a string s, and the second line contains a string t.
# The lengths of both strings do not exceed 1000.
# The strings consist of lowercase Latin letters.

# -- Example 1 --
# INPUT:
# abacaba
# abaabc
# OUTPUT:
# 2

# -- Example 2 --
# INPUT:
# innokentiy
# innnokkentia
# OUTPUT:
# 3

# -- SOLUTION OPERATING PRINCIPLE --
# The shortest Levenshtein distance is determined using the Wagner-Fischer algorithm.

# -- SOLUTION TIME COMPLEXITY --
# Requires O(m*n) time, where (m, n) are the lengths of the two strings being compared.

# -- SOLUTION SPACE COMPLEXITY --
# Requires O(m*n) additional memory, where (m, n) are the lengths of the two strings being compared.


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

