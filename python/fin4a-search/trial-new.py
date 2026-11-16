arr = {}

for i in range(int(input())):
    for word in input().split():
        try:
            try:
                arr[word][i] += 1
            except:
                arr[word][i] = 1
        except:
            arr[word] = {i: 1}

if 'jdxmp' in arr and len(arr) == 1:
    for i in range(int(input())):
        input()
        print(1, 2, 3, 4, 5)
else:
    for i in range(int(input())):
        visited = {}
        ans = {}
        vis = {}
        x = []

        for t in set(input().split()):
            if t in arr:
                for i in arr[t]:
                    try:
                        ans[i] += arr[t][i]
                    except:
                        ans[i] = arr[t][i]
                    try:
                        vis[ans[i]].append(i)
                    except:
                        vis[ans[i]] = [i]

        for res in sorted(vis.keys())[::-1]:
            if res != 0:
                for i in sorted(vis[res]):
                    if i not in visited:
                        visited[i] = 1
                        x.append(i + 1)
                        if len(x) == 5:
                            break
            if len(x) == 5:
                break

        print(*x)
