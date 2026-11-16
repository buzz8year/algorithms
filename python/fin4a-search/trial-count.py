def count_rel(subs, docs):
    data = dict()
    for sub in subs:
        if sub not in data.keys():
            data[sub] = dict()

        cnt = 0
        for doc in docs:
            cnt += 1
            if doc not in data[sub].keys():
                data[sub][cnt] = 0

            for word in sub.split():
                if word in doc.split():
                    data[sub][cnt] += 1
        print(data[sub])
    res = []
    for k in data.values():
        tuples = sorted(k.items(), key=lambda x: x[1], reverse=True)
        res.append(tuples)

    return res


if __name__ == '__main__':
    docs, subs = [], []

    n = int(input())
    for i in range(n):
        docs.append(input())

    m = int(input())
    for j in range(m):
        subs.append(input())

    for sub_iso in count_rel(subs, docs):
        row = ''
        for t in range(len(sub_iso)):
            if sub_iso[t][1] > 0 and t < 5:
                row += str(sub_iso[t][0]) + ' '
        print(row)
