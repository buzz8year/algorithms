def get_max_prefix(words):
    if len(words) == 0:
        return 0

    first_word = words[0]
    for l in range(len(first_word)):
        # print(first_word, l)
        for i in range(len(words)):
            if l == len(words[i]):
                return l
            if words[i][l] != first_word[l]:
                return l

    return len(first_word)


if __name__ == '__main__':
    n = int(input())

    words = []
    for _ in range(n):
        words.append(input())

    print(get_max_prefix(words))

