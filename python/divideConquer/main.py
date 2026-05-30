def fun(array, left, right, value):
    if left >= right:
        return 0
    else:
        if left == right - 1:
            if array[left] == value:
                return 1
            else:
                return 0
        else:
            middle = (left + right) // 2
            return fun(array, left, middle, value) + fun(array, middle, right, value)


if __name__ == '__main__':
    res = fun([1, 1, 1, 2, 2], 1, 3, 1)
    print(res)
