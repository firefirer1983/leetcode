test = [2, 7, 11, 15]


def two_sum_by_hash(nums, target):
    h = {}
    for i, num in enumerate(nums):
        if (target - num) in h:
            return h[target - num], i
        else:
            h[num] = i


def two_sum(nums, target):
    i = 0
    while nums:
        num = nums.pop(0)
        if (target - num) in nums[i:]:
            return i, i + 1 + nums.index(target - num)
        i += 1


if __name__ == "__main__":
    print(two_sum(test, 9))
