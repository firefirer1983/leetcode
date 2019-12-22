class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        s = str(x)
        head = 0
        tail = len(s) - 1
        while tail > head:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    tst = 113
    ans = sol.isPalindrome(tst)
    print(ans)
