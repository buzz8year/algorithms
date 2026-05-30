class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return (self.start, self.end) > (other.start, other.end)


def merge(intervals):
    intervals = sorted(intervals)
    merged = []
    for i in intervals:
        start, end = i.start, i.end
        if len(merged) == 0 or start > merged[-1].end:
            merged.append(Interval(start, end))
        elif end > merged[-1].end:
            merged[-1].end = end

    return merged[0].start


if __name__ == '__main__':
    n = int(input())

    intervals = []
    for _ in range(n):
        start, end = input().split()
        intervals.append(Interval(start, end))

    print(merge(intervals))
