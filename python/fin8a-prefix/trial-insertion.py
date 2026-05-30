def get_string(s, insertions):
    result = ''
    current = 0
    for pos, row in insertions:
        while current < pos:
            result += s[current]
            current += 1

        if current == pos:
            result += row

    for i in range(current, len(s)):
        result += s[i]

    return result


if __name__ == '__main__':
    s = input()
    n = int(input())

    insertions = []
    for _ in range(n):
        row, pos = input().split()
        insertions.append((int(pos), row))

    print(get_string(s, sorted(insertions)))
