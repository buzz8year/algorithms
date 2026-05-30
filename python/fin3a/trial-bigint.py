class Struc():
    def __init__(self, cnum):
        self.cnum = cnum

    def __lt__(self, other):
        return self.cnum + other.cnum > other.cnum + self.cnum


def compare(lhs, rhs):
    return lhs + rhs > rhs + lhs


def get_big_number(data):
    result = ''
    for s in sorted(data):
        result += s.cnum
    return result


if __name__ == '__main__':
    n = int(input())
    data = [Struc(i) for i in input().split()]

    print(get_big_number(data))
