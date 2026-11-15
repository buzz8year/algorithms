# -- STATEMENT --
# A table tennis tournament was held at the training camp.
# John won n matches, earning a certain number of points for each one.
# John began to wonder whether it is possible to divide all the points
# he earned during the tournament into two sets such that
# the sum of the points in each set is the same.

# -- INPUT FORMAT --
# The first line contains an integer n (0 ≤ n ≤ 300) — the number of games won.
# The second line contains n non-negative integers, separated by spaces,
# each not exceeding 300 — the points earned in the games.

# -- OUTPUT FORMAT --
# Output True if such a partition is possible, otherwise output False.

# -- Example 1 --
# INPUT:
# 4
# 1 5 7 1
# OUTPUT:
# True

# -- Example 2 --
# INPUT:
# 3
# 2 10 9
# OUTPUT:
# False

# -- SOLUTION OPERATING PRINCIPLE --
# We select a middle element from the array. Using recursion, we compare all the elements to determine
# whether it is possible to partition the elements into two groups with equal sums.

# -- SOLUTION TIME COMPLEXITY --
# It requires O(n*log(n)) time, where n is the number of elements in the array.

# -- SOLUTION SPACE COMPLEXITY --
# It requires O(n) additional memory, where n is the number of elements in the array.


def is_splitable(arr, value, start=0):

    if value == 0:
        return True

    n = len(arr)
    for i in range(start, n):
        if arr[i] <= value and is_splitable(arr, value - arr[i], i + 1):
            return True

    return False


if __name__ == '__main__':

    n = int(input())
    scores = [int(i) for i in input().split()]
    total = sum(scores)

    if total % 2 != 0:
        result = False
    else:
        half = total // 2
        result = is_splitable(scores, half)