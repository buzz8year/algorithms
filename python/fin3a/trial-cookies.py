def get_children(children, cookies):
    children = sorted(children, reverse=True)
    cookies = sorted(cookies, reverse=True)

    # print(children, cookies)

    count = 0
    while len(children) > 0 and len(cookies) > 0:
        if cookies[-1] >= children[-1]:
            count += 1
            children.pop()
        cookies.pop()

    return count


if __name__ == '__main__':
    n = int(input())
    children = [int(i) for i in input().split()]

    m = int(input())
    cookies = [int(i) for i in input().split()]

    print(get_children(children, cookies))
