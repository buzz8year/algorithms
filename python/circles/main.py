def unique(str_list):
    unique_list = []

    for s in str_list:
        if s not in unique_list:
            unique_list.append(s)

    return unique_list


if __name__ == '__main__':
    n = int(input())

    str_list = []
    for i in range(n):
        str_list.append(input())

    for k in unique(str_list):
        print(k)


