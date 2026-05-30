from typing import List, Tuple


def moving_average(array_given: List[int], window_given: int) -> List[float]:
    data = []
    lena = len(array_given) - window_given

    summa = sum(array_given[0:window_given])
    data.append(float(summa / window_given))

    for i in range(0, lena):
        summa -= array_given[i]
        summa += array_given[i + window_given]
        data.append(float(summa / window_given))

    return data


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    array_given = list(map(int, input().strip().split()))
    window_given = int(input())
    return array_given, window_given


if __name__ == '__main__':
    arr, window_size = read_input()
    print(" ".join(map(str, moving_average(arr, window_size))))
