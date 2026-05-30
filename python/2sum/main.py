def find_sum_naive(nums, target):
    l: int = len(nums)
    for i in range(l):
        for k in range(i + 1, l):
            if nums[i] + nums[k] == target:
                return [i, k]
    return []


def find_sum(nums, target):
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            print(numToIndex)
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []


def get_nums():
    return [3, 1, 4, 5, 5, 6, 7, 13, 11, 3]


def get_target():
    return 6


if __name__ == '__main__':
    print(find_sum(get_nums(), get_target()))
