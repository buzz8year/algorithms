def sort(arr):
    counter = [0] * 3
    for val in arr:
        counter[val] += 1

    return counter


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]

    colors = sort(arr)
    # print(colors)
    for i in range(len(colors)):
        print((str(i) + ' ') * colors[i], end='')
