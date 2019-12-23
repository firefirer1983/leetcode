#!/usr/bin/env python3
class Solution:
    def intToRoman(self, num):
        roman = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        weight = 1000
        ret = ""
        while weight > 0:
            unit = roman[weight]
            r = int(num / weight)
            if r == 0:
                pass
            elif r <= 3:
                ret += r * unit
            elif r < 5:
                ret += (5 - r) * unit + roman[weight * 5]
            elif r <= 8:
                ret += roman[weight * 5] + (r - 5) * unit
            else:
                ret += (10 - r) * unit + roman[weight * 10]
            num -= r * weight
            weight = int(weight / 10)

        return ret


if __name__ == "__main__":
    sol = Solution()
    tst = 113
    ans = sol.intToRoman(tst)
    print(ans)
