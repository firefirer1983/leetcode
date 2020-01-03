class Solution:
    def threeSum(self, nums):
        sums = []
        htb = {}
        nums = sorted(nums)
        for i, v in enumerate(nums):
            if v not in htb:
                htb[v] = i

        tail = len(nums) - 1
        print(nums)
        prev_tail = None
        while tail > 1 and nums[tail] >= 0:
            if nums[tail] != prev_tail:
                head = 0
                prev_head = None
                while (tail - head > 1) and nums[head] <= 0:
                    if nums[head] != prev_head:
                        comp = -(nums[head] + nums[tail])
                        if comp in htb:
                            pos = htb[comp]
                            if pos == head or pos == tail:
                                offset = pos + 1
                                while offset < len(nums):
                                    if nums[offset] == comp:
                                        sums.append(
                                            [nums[head], comp, nums[tail]]
                                        )
                                        break
                                    offset += 1
                            elif head < pos < tail:
                                sums.append([nums[head], comp, nums[tail]])
                        prev_head = nums[head]
                    head += 1
                prev_tail = nums[tail]
            tail -= 1

        return sums


if __name__ == "__main__":
    tst = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    ans = sol.threeSum(tst)
    print("answer:", ans)
