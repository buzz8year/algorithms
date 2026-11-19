# -- PROBLEM STATEMENT
# Alla made a mistake when copying data from one data structure to another.
# She stored an array of numbers in a ring buffer. The array was sorted in ascending order,
# and it was possible to find an element in it in logarithmic time.
# Alla copied the data from the ring buffer to a regular array,
# but she shifted the data of the original sorted sequence (although the array could still remain sorted).
# Nevertheless, it is necessary to ensure that it is possible to find an element in it in O(log(n)).
# It can be assumed that the array contains only unique elements.
# You are required to implement a function that performs a search in the broken array.
# Please note that you are not required to read the data or output the answer.

# -- Input format
# The function takes an array of natural numbers and the target number k.
# The length of the array does not exceed 10000. The array elements and the number k do not exceed 10000 in value.
# In the examples:
# The first line contains the number n — the length of the array.
# The second line contains the positive number k — the target element.
# Next, n natural numbers are written in a line separated by spaces — the array elements.

# -- Output format
# The function should return the index of the element equal to k,
# if such an element exists in the array (numbering starts from zero).
# If the element is not found, the function should return −1.
# The array cannot be modified. To eliminate inefficient solutions,
# your function will be called between 100,000 and 1,000,000 times.

# -- Example 1 --
# INPUT:
# 9
# 5
# 19 21 100 101 1 4 5 7 12
# OUTPUT:
# 6

# -- Example 2 --
# INPUT:
# 2
# 1
# 5 1
# OUTPUT:
# 1


# -- OPERATING PRINCIPLE --
# Sorting is performed using Hoare's quicksort algorithm.
#
# -- TIME COMPLEXITY --
# The time complexity of the algorithm is O(n*log(n)), as the pivot element divides the array in half.
#
# -- SPACE COMPLEXITY --
# An array containing k elements occupies O(k) memory.


def sort_name(items):
    if len(items) < 2:
        return items
    left, center, right = partition(items, 0)
    return sort_name(right) + center + sort_name(left)


def sort_penal(items):
    if len(items) < 2:
        return items
    right, center, left = partition(items, 2)
    return sort_penal(left) + sort_name(center) + sort_penal(right)


def sort_rate(items):
    if len(items) < 2:
        return items
    left, center, right = partition(items, 1)
    return sort_rate(left) + sort_penal(center) + sort_rate(right)


def partition(items, key):
    left, center, right = [], [], []
    pivot = items[len(items) // 2]

    for item in items:
        if item[key] > pivot[key]:
            left.append(item)
        elif item[key] == pivot[key]:
            center.append(item)
        else:
            right.append(item)

    return left, center, right


if __name__ == '__main__':
    n = int(input())

    lists = []
    for i in range(n):
        inp = input().split()
        lists.append([inp[0], int(inp[1]), int(inp[2])])

    lists = sort_rate(lists)

    for l in lists:
        print(l[0])
