def transform(word):
    result = ''
    for ch in word:
        if ord(ch) % 2 == 0:
            result += ch
    return result


def compare(lhs, rhs):
    if lhs < rhs:
        return -1
    elif lhs == rhs:
        return 0
    else:
        return 1


if __name__ == '__main__':
    s = input()
    t = input()

    print(compare(transform(s), transform(t)))
