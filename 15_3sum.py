#!/usr/bin/env python3


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        smallest_positive = len(nums) - 1
        largest_negative = 0
        while smallest_positive != largest_negative:
            if nums[smallest_positive] > 0:
                smallest_positive -= 1
            if nums[largest_negative] < 0:
                largest_negative += 1

        return []


if __name__ == "__main__":
    sol = Solution()
    tst = [-1, 0, 1, 2, -1, -4]
    ans = sol.threeSum(tst)
    print(ans)
