def get_count_find_tree(n, open=0, close=0):
    if open + close == n * 2:
        return 1

    result = 0

    if open < n:
        result += get_count_find_tree(n, open + 1, close)
    if open > close:
        result += get_count_find_tree(n, open, close + 1)

    return result


if __name__ == '__main__':
    print(get_count_find_tree(int(input())))
