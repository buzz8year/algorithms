# -- PROBLEM STATEMENT --
# In this task, you need to implement heap sort. At the same time, you must implement the heap yourself;
# you cannot use the implementations available in the language.
# First, it is recommended to solve problems related to sifting down and up.

# John decided to organize a sports programming competition to find talented interns.
# The tasks have been selected, the participants have been registered, and the tests have been written.
# All that remains is to figure out how the winner will be determined at the end of the competition.
# Each participant has a unique login. When the competition ends, two metrics will be associated with it:
# the number of solved problems Pᵢ and the penalty amount Fᵢ. The penalty is charged for unsuccessful
# attempts and the time spent on the task.
# John decided to sort the results table as follows: when comparing two participants,
# the one with more solved problems will be ranked higher. If the number of solved problems is the same,
# the participant with the lower penalty will be ranked first. If the penalties also match,
# then the first one will be the one whose login comes first in alphabetical (lexicographic) order.
# John ordered hoodies for the winners and went to the store for them the day before.
# In his absence, he instructed you to implement a heap sorting algorithm (English Heapsort) for the results table.

# -- INPUT FORMAT --
# The first line contains the number of participants n, 1≤n≤100000.
# Each of the following n lines contains information about one participant.
# Fᵢ and Pᵢ are integers in the range from 0 to 10^9.
# The i-th participant is described by three parameters:
# - a unique login (a string of lowercase Latin letters no longer than 20 characters)
# - the number of solved problems Pᵢ
# - the penalty Fᵢ


# -- OUTPUT FORMAT --
# For the sorted list of participants, output their logins in order, one per line.

# -- Example 1 --
# INPUT:
# 5
# alla 4 100
# gena 6 1000
# gosha 2 90
# rita 2 90
# timofey 4 80
# OUTPUT:
# gena
# timofey
# alla
# gosha
# rita

# -- Example 2 --
# INPUT:
# 5
# alla 0 0
# gena 0 0
# gosha 0 0
# rita 0 0
# timofey 0 0
# OUTPUT:
# alla
# gena
# gosha
# rita
# timofey

# -- SOLUTION WORKING PRINCIPLE --
# Sorting is carried out using the heapsort method.

# -- SOLUTION TIME COMPLEXITY --
# The time complexity of the algorithm is O(n*log(n)).

# -- SOLUTION SPACE COMPLEXITY --
# O(log(n)) additional memory will be required.

def heapify(tuples, size, root):
    node = root
    left = (2 * root) + 1
    rght = (2 * root) + 2

    if left < size and tuples[left] > tuples[node]: node = left
    if rght < size and tuples[rght] > tuples[node]: node = rght
    if node != root:
        tuples[root], tuples[node] = tuples[node], tuples[root]
        heapify(tuples, size, node)


def heapsort(tuples):
    size = len(tuples)
    for i in range(size, -1, -1):
        heapify(tuples, size, i)

    for i in range(size - 1, 0, -1):
        tuples[i], tuples[0] = tuples[0], tuples[i]
        heapify(tuples, i, 0)


if __name__ == '__main__':
    n = int(input())

    tuples = []
    for i in range(n):
        inp = input().split()
        tuples.append((-int(inp[1]), int(inp[2]), inp[0]))

    heapsort(tuples)

    for t in tuples:
        print(t[2])
