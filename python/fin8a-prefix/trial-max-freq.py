def get_max_freq_string(counter):
    result = ''
    frequency = 0
    for word, count in counter.items():
        if count > frequency:
            result = word
            frequency = count

        if count == frequency and result > word:
            result = word

    return result


if __name__ == '__main__':
    n = int(input())

    rows = dict()
    for i in range(n):
        word = input()
        rows[word] = rows.get(word, 0) + 1

    print(get_max_freq_string(rows))
