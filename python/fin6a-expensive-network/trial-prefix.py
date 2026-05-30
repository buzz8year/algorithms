v = []
mn = 10**8
for j in range(int(input())):
    s = input()

    q = []
    d = []
    ind = []

    s += '1[]'

    for i in range(len(s)):
        if s[i] == ']':
            ss = ''
            while len(q) and q[-1] != '[':
                if q[-1] == '$':
                    ss += d[-1]
                    d.pop()
                    ind.pop()
                else:
                    ss += q[-1]
                q.pop()
            q.pop()

            k = ''
            while len(q) and q[-1].isdigit():
                k += q[-1]
                q.pop()

            sss = ''
            while len(q) and q[-1] != '[':
                if q[-1] == '$':
                    sss += d[-1]
                    d.pop()
                    ind.pop()
                else:
                    sss += q[-1]
                q.pop()

            q.append('$')
            ind.append(len(q) - 1)
            d.append(int(k) * ss + sss)

            continue

        q.append(s[i])

    mn = min(mn, len(d[-1]))
    v.append(d[-1])


go = 1
ans = ''

for i in range(mn):
    k = v[0][-1 - i]
    for j in v:
        if j[-1 - i] != k:
            go = 0
            break
    if not go:
        break
    ans += v[0][-1 - i]

print(ans)
