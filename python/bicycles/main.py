def bin_search(arr, x, left, right):
    if left >= right:
        return -2

    mid = (left + right) // 2

    if arr[mid] >= x:
        if mid == 0 or arr[mid - 1] < x:
            return mid
        else:
            return bin_search(arr, x, left, mid)
    else:
        return bin_search(arr, x, mid + 1, right)


def shop_days(bank, price):
    days = []

    day1 = bin_search(bank, price, 0, len(bank)) + 1
    day2 = bin_search(bank, price * 2, 0, len(bank)) + 1

    days.append(str(day1))
    days.append(str(day2))

    return days


if __name__ == '__main__':
    n = int(input())
    bank = [int(i) for i in input().split()]
    price = int(input())

    res = " ".join(shop_days(bank, price))

    print(res)

