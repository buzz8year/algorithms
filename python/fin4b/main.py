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
    while n > 0:
        n -= 1

        command = input().split()
        key = int(command[1])
        val = command[2] if len(command) == 3 else None
        fun = getattr(ht, command[0])

        res = fun(key, val)
        if command[0] in ['get', 'delete']:
            print(res)
