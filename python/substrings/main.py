def get_unique_len(str):
    letters = dict()
    result = 0
    prev = 0

    for i in range(len(str)):
        if str[i] not in letters.keys():
            letters[str[i]] = 0

        prev = max(prev, letters[str[i]])
        letters[str[i]] = i + 1
        result = max(result, i + 1 - prev)

        print(str[i], result, letters)

    return result


if __name__ == '__main__':
    str = input()
    print(get_unique_len(str))

