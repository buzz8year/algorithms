def reverse(word):
    left = 0
    rght = len(word) - 1
    # print(word)
    word = list(word)
    while left < rght:
        word[left], word[rght] = word[rght], word[left]
        left += 1
        rght -= 1

    return ''.join(word)


def get_palyndrom(word):
    counter = dict()
    for ch in word:
        counter[ch] = counter.get(ch, 0) + 1

    counter = dict(sorted(counter.items()))

    result = ''
    center = '%'

    # print(counter)

    for ch, count in counter.items():
        # print(ch, count)
        if count % 2 == 0:
            result += ch * (count // 2)
        else:
            if center == '%':
                center = ch
            if count > 1:
                result += ch * ((count - 1) // 2)

    if center != '%':
        return result + center + reverse(result)
    else:
        return result + reverse(result)


if __name__ == '__main__':
    word = input()
    print(get_palyndrom(word))
