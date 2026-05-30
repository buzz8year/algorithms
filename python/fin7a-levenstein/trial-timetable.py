class Lesson:
    def __init__(self, start, end):
        self.display = start + ' ' + end
        self.start = float(start)
        self.end = float(end)

    def __lt__(self, other):
        if self.end == other.end:
            return self.start < other.start
        return self.end < other.end


def get_timetable(lessons):
    lessons.sort()
    result = set()
    prev = Lesson('0', '0')
    for lesson in lessons:
        if lesson.start >= prev.end:
            prev = lesson
            result.add(prev)
    return result


if __name__ == '__main__':
    n = int(input())

    lessons = []
    for _ in range(n):
        start, end = input().split()
        lesson = Lesson(start, end)
        lessons.append(lesson)

        # print(lesson.start, lesson.end)

    results = sorted(get_timetable(lessons))
    print(len(results))
    for i in results:
        print(i.display)
