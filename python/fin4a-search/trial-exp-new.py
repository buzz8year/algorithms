class Document:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.vals = [None] * self.size
        self.sums = [0] * self.size

    def __contains__(self, val):
        return val in self.vals

    def hash_function(self, key):
        return key % self.size

    def find_position_by_val(self, val, key=None):
        if val in self.vals:
            return self.vals.index(val)
        elif key is not None:
            return self.find_position(key)

    def find_position(self, key):
        position = self.hash_function(key)
        while self.keys[position] is not None and self.keys[position] != key:
            position = (position + 1) % self.size
        return position

    def zip_sums(self):
        return dict(zip(self.vals, self.sums))

    def put(self, key, val):
        position = self.find_position_by_val(val, key)
        if self.vals[position] == val:
            self.vals[position] = val
            self.sums[position] += 1
        else:
            self.keys[position] = key
            self.vals[position] = val
            self.sums[position] = 1


class Query:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.vals = [None] * self.size
        self.rels = {}

    def hash_function(self, key):
        return key % self.size

    def find_position_by_val(self, val, key=None):
        if val in self.vals:
            return self.vals.index(val)
        elif key is not None:
            return self.find_position(key)

    def find_position(self, key):
        position = self.hash_function(key)
        while self.keys[position] is not None and self.keys[position] != key:
            position = (position + 1) % self.size
        return position

    def put(self, key, val):
        position = self.find_position_by_val(val, key)
        if self.vals[position] == val:
            self.vals[position] = val
        else:
            self.keys[position] = key
            self.vals[position] = val

    def get_rels(self):
        return sorted(self.rels.items(), key=lambda x: x[1], reverse=True)[:5]

    def query2doc(self, doc):
        res = 0
        for val in self.vals:
            if val in doc:
                res += doc.zip_sums()[val]
        return res


class TaskManager:
    def __init__(self):
        self.docs = []
        self.ques = []

    def new_doc(self, string):
        doc = Document(pow(10, 3) + 3)
        words = string.split()
        for i in range(len(words)):
            doc.put(i, words[i])
        self.docs.append(doc)

    def new_query(self, string):
        query = Query(pow(10, 2) + 3)
        words = string.split()
        for i in range(len(words)):
            query.put(i, words[i])
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
