from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    sorted(arr)
    cur_left = 0
    cur_right = len(arr) - 1
    while cur_left < cur_right:
        left = arr[cur_left]
        right = arr[cur_right]
        sum = left + right
        if (sum == target_sum):
            return [left, right]
        if (sum < target_sum):
            cur_left += 1
        else:
            cur_right -= 1
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


if __name__ == '__main__':
    arr, target_sum = read_input()
    print_result(two_sum(arr, target_sum))
