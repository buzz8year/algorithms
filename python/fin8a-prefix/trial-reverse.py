def reverse(words):
    left = 0
    rght = len(words) - 1
    while left < rght:
        words[left], words[rght] = words[rght], words[left]
        left += 1
        rght -= 1

    return words


if __name__ == '__main__':
    words = input().split()
    print(' '.join(reverse(words)))
