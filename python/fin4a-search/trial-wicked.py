def check(tmpl, word):
    if len(tmpl) != len(word):
        return False

    tiw = dict()
    wit = dict()

    for i in range(len(word)):
        if word[i] not in tiw:
            tiw[word[i]] = tmpl[i]
        elif tiw[word[i]] != tmpl[i]:
            return False

        if tmpl[i] not in wit:
            wit[tmpl[i]] = word[i]
        elif wit[tmpl[i]] != word[i]:
            return False

    return True


if __name__ == '__main__':
    s = input()
    t = input()

    print('YES' if check(s, t) else 'NO')
