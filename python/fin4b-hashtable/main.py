# -- PROBLEM STATEMENT
# John, as a good manager, stores information about his employees’ salaries in a database and constantly updates it.
# He has tasked you with writing an implementation of a hash table to store the database with employees’ salaries in it.

# The table stores unique keys.
# The hash table must support the following operations:
# - put key value — adding a key-value pair. If the given key already exists in the table, the corresponding value is updated.
# - get key — retrieving the value by key. If the key is not in the table, output “None”. Otherwise, output the found value.
# - delete key –— delete the key from the table. If such a key does not exist, output “None”; otherwise, output the value stored for this key and delete the key.

# -- Implementation requirements:
# - You cannot use the hash table implementations available in programming languages (std::unordered_map in C++, dict in Python, HashMap in Java, etc.).
# - Collisions should be resolved using the chaining method or open addressing.
# - All operations must be performed in O(1) on average.
# - It is not required to support rehashing and scaling of the hash table.
# - Keys and values, employee IDs and their salaries, are integers. It is not required to support arbitrary hashed types.

# -- Input format
# The first row contains the total number of queries to the table n (1≤n≤10^6).
# The following n lines contain requests, which come in three types — get, put, delete — as described in the condition.
# All keys and values are integers not exceeding 10^9 modulo. The numbers can also be negative.
# For any sequence of commands, the number of keys in the hash table cannot exceed 10^5.

# -- Output format --
# For each get and delete request, output the response on a separate line.

# -- Example 1 --
# INPUT:
# 10
# get 1
# put 1 10
# put 2 4
# get 1
# get 2
# delete 2
# get 2
# put 1 5
# get 1
# delete 2
# OUTPUT:
# None
# 10
# 4
# 4
# None
# 5
# None

# -- Example 2 --
# INPUT:
# 8
# get 9
# delete 9
# put 9 1
# get 9
# put 9 2
# get 9
# put 9 3
# get 9
# OUTPUT:
# None
# None
# 1
# 2
# 3

# -- SOLUTION OPERATING PRINCIPLE --
# Implementation of the “hash table” structure

# -- SOLUTION TIME COMPLEXITY --
# The time complexity of the get, put, and delete methods is O(1).

# -- SOLUTION SPACE COMPLEXITY --
# An array containing k elements occupies O(k) memory.

class HashTable:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.vals = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def find_position(self, key):
        position = self.hash_function(key)

        while self.keys[position] is not None and self.keys[position] != key:
            position = (position + 1) % self.size

        return position

    def put(self, key, val):
        position = self.find_position(key)

        if self.keys[position] == key:
            self.vals[position] = val

        else:
            self.keys[position] = key
            self.vals[position] = val

    def get(self, key, val=None):
        position = self.find_position(key)

        if self.keys[position] is not None:
            val = self.vals[position]

        return val

    def delete(self, key, val=None):
        position = self.find_position(key)

        if self.keys[position] == key:
            val = self.vals[position]
            self.vals[position] = None

        return val


if __name__ == '__main__':
    ht = HashTable(pow(10, 6) + 3)
    n = int(input())

    for _ in range(n):
        command = input().split()
        param1 = int(command[1])
        param2 = command[2] if len(command) == 3 else None

        fun = getattr(ht, command[0])
        res = fun(param1, param2)

        if command[0] in ['get', 'delete']:
            print(res)

