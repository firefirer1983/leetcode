#!/usr/bin/env python3
class Solution:
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        length = len(s)
        pos = length - 1
        num = 0
        sign = 1
        prev = 1
        while pos >= 0:

            val = roman[s[pos]]

            if val < prev:
                sign *= -1
            elif val > prev:
                sign = 1
            prev = val
            num += sign * val
            pos -= 1

        return num


if __name__ == "__main__":
    sol = Solution()
    tst = "XLVIII"
    ans = sol.romanToInt(tst)
    print(ans)
