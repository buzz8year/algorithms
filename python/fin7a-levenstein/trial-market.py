def test(n, prices):
    profit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == '__main__':
    n = int(input())
    prices = [int(i) for i in input().split()]

    print(test(n, prices))
