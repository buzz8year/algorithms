def dfs(digits, alphabet, result, buffer=''):
    if len(buffer) == len(digits):
        result.append(buffer)
        return

    # print(alphabet[int(digits[len(buffer)])])
    for letter in alphabet[int(digits[len(buffer)])]:
        dfs(digits, alphabet, result, buffer + letter)


def combine(digits, alphabet):
    combinations = []
    dfs(digits, alphabet, combinations)
    return combinations


if __name__ == '__main__':
    alphabet = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    digits = input()

    combs = combine(digits, alphabet)
    print(' '.join(combs))

