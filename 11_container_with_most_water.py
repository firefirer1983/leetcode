class Solution:
    def maxArea(self, height):
        max_area = 0
        length = len(height)
        max_height = 0

        for i in range(length - 1):

            if height[i] <= max_height:
                continue

            j = i + 1

            while True:
                size = (j - i) * (min(height[i], height[j]))
                if size > max_area:
                    max_area = size
                    max_height = height[i]
                j += 1

                if j == length:
                    break
        return max_area

    def maxArea2(self, height):
        length = len(height)
        head = 0
        tail = length - 1
        water = 0
        for i in range(length):
            if height[head] > height[tail]:
                size = height[tail] * (tail - head)
                tail -= 1
            else:
                size = height[head] * (tail - head)
                head += 1
            if size > water:
                water = size
        return water


if __name__ == "__main__":
    sol = Solution()
    # tst = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # tst = [6, 4, 3, 1, 4, 6, 99, 62, 1, 2, 6]
    tst = [9, 6, 14, 11, 2, 2, 4, 9, 3, 8]
    ans = sol.maxArea2(tst)
    print(ans)
