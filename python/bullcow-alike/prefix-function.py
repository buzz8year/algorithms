def find(s):
    pres = [0] * len(s)

    for i in range(1, len(s)):
        k = pres[i - 1]

        while k > 0 and s[k] != s[i]:
            k = pres[k - 1]

        if s[i] == s[k]:
            k += 1

        pres[i] = k

    return pres


if __name__ == '__main__':
    s = input()
    print(*find(s))
