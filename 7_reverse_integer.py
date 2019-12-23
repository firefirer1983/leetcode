#!/usr/bin/env python3


class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        
        if x == 2**31:
            return 0
        sign = int(x / abs(x))
        val = abs(x)
        tmp = []
        while val:
            tmp.insert(0, val % 10)
            val = int(val/10)
        rev = 0
        for i, d in enumerate(tmp):
            rev += d*(10**i)
        if rev > 2147483647:
            return 0
        return rev * sign

    def best_reverse(self, x):
        sign = int(x / abs(x))
        rev = int(str(abs(x))[::-1])
        if rev > 2147483647:
            return 0
        return rev *sign


if __name__ == "__main__":
    tst = 4096
    sol = Solution()
    ans = sol.best_reverse(tst)
    print(ans)
