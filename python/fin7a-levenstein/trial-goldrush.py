def get_max(items, capacity):
    items.sort(reverse=True)
    result = 0

    for item in items:
        if capacity == 0:
            break
        max_weight = min(capacity, item[1])
        result += max_weight * item[0]
        capacity -= max_weight

    return result


if __name__ == '__main__':
    capacity = int(input())
    n = int(input())

    items = []
    for _ in range(n):
        cost, weight = (int(i) for i in input().split())
        items.append((cost, weight))

    print(get_max(items, capacity))
