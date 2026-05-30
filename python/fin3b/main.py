# 64684565

# -- ПРИНЦИП РАБОТЫ --
# Сортировка осуществляется методом быстрой сортировки Хоара.
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Временная сложность алгоритма O(n*log(n)), т.к. опорный элемент делит массив пополам.
#
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Массив содержащий k элементов, занимает O(k) памяти.


# -- ВОПРОСЫ --
# Убрал sorted() и поправил while/for
# А вот насчет единного компаратора почему-то не могу понять.
# Кажется, как я делаю, с рекурсией, по трем признакам одним методом не отсортировать.


def sort_name(items):
    if len(items) < 2:
        return items
    left, center, right = partition(items, 0)
    return sort_name(right) + center + sort_name(left)


def sort_penal(items):
    if len(items) < 2:
        return items
    right, center, left = partition(items, 2)
    return sort_penal(left) + sort_name(center) + sort_penal(right)


def sort_rate(items):
    if len(items) < 2:
        return items
    left, center, right = partition(items, 1)
    return sort_rate(left) + sort_penal(center) + sort_rate(right)


def partition(items, key):
    left, center, right = [], [], []
    pivot = items[len(items) // 2]

    for item in items:
        if item[key] > pivot[key]:
            left.append(item)
        elif item[key] == pivot[key]:
            center.append(item)
        else:
            right.append(item)

    return left, center, right


if __name__ == '__main__':
    n = int(input())

    lists = []
    for i in range(n):
        inp = input().split()
        lists.append([inp[0], int(inp[1]), int(inp[2])])

    lists = sort_rate(lists)

    for l in lists:
        print(l[0])
