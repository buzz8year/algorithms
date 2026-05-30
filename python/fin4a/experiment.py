class Document:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.vals = [None] * self.size
        self.sums = [0] * self.size

    def __contains__(self, val):
        return True if val in self.vals else False

    def hash_function(self, key):
        return key % self.size

    def find_position_by_val(self, val, key=None):
        if val in self.vals:
            return self.vals.index(val)
        elif key is not None:
            return self.find_position(key)
        else:
            raise ValueError('Can\'t be true!')

    def find_position(self, key):
        position = self.hash_function(key)
        while self.keys[position] is not None and self.keys[position] != key:
            position = (position + 1) % self.size
        return position

    def zip_sums(self):
        return dict(zip(self.vals, self.sums))

    # def zip_all(self):
    #     return dict(zip(self.keys, self.vals))

    # def get_sum(self, key):
    #     return self.sums[key]

    def get_sum_by_val(self, val):
        position = self.find_position_by_val(val)
        return self.sums[position]

    # def get(self, key, val=None):
    #     position = self.find_position(key)
    #     if self.keys[position] is not None:
    #         val = self.vals[position]
    #     return val

    # def get_key_by_val(self, val, key=None):
    #     position = self.find_position_by_val(val)
    #     if self.keys[position] is not None:
    #         key = self.keys[position]
    #     return key

    # def put(self, key, val):
    #     position = self.find_position(key)
    #     if self.keys[position] == key:
    #         self.vals[position] = val
    #     else:
    #         self.keys[position] = key
    #         self.vals[position] = val

    def put_by_val(self, key, val):
        position = self.find_position_by_val(val, key)
        if self.vals[position] == val:
            self.vals[position] = val
            self.sums[position] += 1
        else:
            self.keys[position] = key
            self.vals[position] = val
            self.sums[position] = 1

    # def delete(self, key, val=None):
    #     position = self.find_position(key)
    #     if self.keys[position] == key:
    #         val = self.vals[position]
    #         self.vals[position] = None
    #     return val


class Query:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.vals = [None] * self.size
        self.sums = [0] * self.size
        self.rels = {}

    def hash_function(self, key):
        return key % self.size

    def find_position_by_val(self, val, key=None):
        if val in self.vals:
            return self.vals.index(val)
        elif key is not None:
            return self.find_position(key)
        else:
            raise ValueError('Can\'t be true!')

    def find_position(self, key):
        position = self.hash_function(key)
        while self.keys[position] is not None and self.keys[position] != key:
            position = (position + 1) % self.size
        return position

    # def zip_sums(self):
    #     return dict(zip(self.vals, self.sums))
    #
    # def zip_all(self):
    #     return dict(zip(self.keys, self.vals))

    # def put(self, key, val):
    #     position = self.find_position(key)
    #     if self.keys[position] == key:
    #         self.vals[position] = val
    #     else:
    #         self.keys[position] = key
    #         self.vals[position] = val

    def put_by_val(self, key, val):
        position = self.find_position_by_val(val, key)
        if self.vals[position] == val:
            self.vals[position] = val
        else:
            self.keys[position] = key
            self.vals[position] = val

    # def get(self, key, val=None):
    #     position = self.find_position(key)
    #     if self.keys[position] is not None:
    #         val = self.vals[position]
    #     return val

    def get_rels(self):
        return sorted(self.rels.items(), key=lambda x: x[1], reverse=True)[:5]

    # def delete(self, key, val=None):
    #     position = self.find_position(key)
    #     if self.keys[position] == key:
    #         val = self.vals[position]
    #         self.vals[position] = None
    #         self.sums[position] = 0
    #     return val

    def query2doc(self, doc):
        res = 0
        for key in self.keys:
            if key is not None:
                position = self.find_position(key)
                word = self.vals[position]
                if word in doc:
                    res += doc.zip_sums()[word]
        return res


class TaskManager:
    def __init__(self):
        self.docs = []
        self.ques = []

    def new_doc(self, string):
        doc = Document(pow(10, 2) + 3)
        words = string.split()
        for i in range(len(words)):
            doc.put_by_val(i, words[i])
        self.docs.append(doc)

    def new_query(self, string):
        query = Query(pow(10, 2) + 3)
        words = string.split()
        for i in range(len(words)):
            query.put_by_val(i, words[i])
        self.ques.append(query)

        for d in range(len(self.docs)):
            query.rels[d + 1] = query.query2doc(self.docs[d])

    def get_docs(self):
        return self.docs

    def get_ques(self):
        return self.ques


if __name__ == '__main__':
    task_man = TaskManager()

    n = int(input())
    for i in range(n):
        task_man.new_doc(input())

    m = int(input())
    for j in range(m):
        task_man.new_query(input())

    for z in task_man.get_ques():
        for y in z.get_rels():
            if y[1] > 0:
                print(y[0], end=" ")
        print("")
