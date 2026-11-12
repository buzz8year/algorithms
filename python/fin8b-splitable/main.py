def is_splitable(text, words):
    parts = [[] for _ in range(26)]

    for part in set(words):
        key = ord(part[0]) - ord('a')
        parts[key].append(part)

    l = len(text)
    res = [0] * (l + 1)
    res[0] = 1

    for i in range(l):
        if not res[i]:
            continue

        key = ord(text[i]) - ord('a')
        for part in parts[key]:
            if text.startswith(part, i):
                res[i + len(part)] = 1

    return bool(res[l])


if __name__ == '__main__':
    text = input()