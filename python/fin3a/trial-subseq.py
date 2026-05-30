def is_sub(template, str):
    i = 0
    for ch in str:
        if i == len(template):
            return True
        if ch == template[i]:
            i += 1
    return i == len(template)


if __name__ == '__main__':
    s = input()
    t = input()

    print(is_sub(s, t))
