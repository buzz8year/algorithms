def can_split(s, arr):
    parts = [[] for _ in range(26)]
    for part in set(arr):
        key = ord(part[0]) - ord('a')
        parts[key].append(part)

    w = len(s)
    res = [0] * (w+1)
    res[0] = 1

    for i in range(w):
        if not res[i]:
            continue
        key = ord(s[i]) - ord('a')
        for part in parts[key]:
            if s.startswith(part, i):
                res[i+len(part)] = 1

    if res[w]:
        return 'YES'
    else:
        return 'NO'


s = input()
n = int(input())

data = []
for i in range(n):
    data.append(input())

print(can_split(s, data))
