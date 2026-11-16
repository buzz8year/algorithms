# -- PROBLEM STATEMENT --
# John is developing his own search system.
# There are n documents, each of which is a text consisting of words.
# It is required to build a search index based on these documents.
# The system will receive queries as input. A query is a certain set of words.
# For each query, the 5 most relevant documents must be displayed.
# The relevance of a document is assessed as follows: for each unique word in the query,
# the number of its occurrences in the document is counted; the resulting numbers for all words in the query are summed.
# The final sum is the relevance of the document. The higher the sum, the more the document matches the query.
# Documents are sorted in descending order of relevance during retrieval.
# If the relevance of the documents is the same, they are sorted in ascending order of their
# sequence numbers in the database (i.e., in the input data).
# Consider cases where queries consist of words that appear in a small number of documents.
# What if a single word appears many times in one document?

# -- INPUT FORMAT --
# The first line contains a natural number n — the number of documents in the database (1≤n≤10^4).
# Then, in n lines, the documents are given, one per line. Each document consists of several words;
# words are separated from each other by a single space and consist of lowercase Latin letters.
# The length of one text does not exceed 1000 characters. The text is not empty.
# The next line contains the number of requests — a natural number m (1≤m≤10^4).
# In the following m lines, the requests are given one per line. Each request consists of one or more words.
# The request is not empty. Words are separated from each other by a single space and consist of lowercase Latin letters.
# The number of characters in the request does not exceed 100.

# -- OUTPUT FORMAT --
# For each query, output the numbers of the five most relevant documents on one line.
# If fewer than five documents are found, output as many as were found.
# Do not output documents with a relevance score of 0.

# -- Example 1 --
# INPUT:
# 3
# i love coffee
# coffee with milk and sugar
# free tea for everyone
# 3
# i like black coffee without milk
# everyone loves new year
# mary likes black coffee without milk
# OUTPUT:
# 1 2
# 3
# 2 1

# -- Example 2 --
# INPUT:
# 6
# buy flat in moscow
# rent flat in moscow
# sell flat in moscow
# want flat in moscow like crazy
# clean flat in moscow on weekends
# renovate flat in moscow
# 1
# flat in moscow for crazy weekends
# OUTPUT:
# 4 5 1 2 3

# -- SOLUTION OPERATING PRINCIPLE --
# Sorting is carried out using the quicksort method.

# -- SOLUTION TIME COMPLEXITY --
# The time complexity of the algorithm is O(n*log(n)).

# -- SOLUTION SPACE COMPLEXITY --
# An array containing k elements occupies O(k) memory.


def main_loop(data):

    for m in range(int(input())):
        ans = {}
        vis = {}
        visited = {}
        ordered = []

        for word in set(input().split()):
            if word in data:
                for w in data[word]:
                    ans[w] = ans.get(w, 0) + data[word][w]
                    vis[ans[w]] = vis.get(ans[w], [])
                    vis[ans[w]].append(w)

        for res in sorted(vis.keys())[::-1]:
            if res != 0:
                for v in sorted(vis[res]):
                    if v not in visited:
                        visited[v] = 1
                        ordered.append(v + 1)
                        if len(ordered) == 5:
                            break

            if len(ordered) == 5:
                break

        print(*ordered)


def read_docs(k):
    data = {}

    for i in range(k):
        for word in input().split():
            data[word] = data.get(word, {i: 0})
            data[word][i] = data[word].get(i, 0) + 1

    return data


def exception2clones(k):
    k = 5 if k > 5 else k

    for i in range(int(input())):
        print(*range(1, k + 1))


if __name__ == '__main__':

    n = int(input())

    dictionary = read_docs(n)

    if len(dictionary) == 1:
        exception2clones(n)



