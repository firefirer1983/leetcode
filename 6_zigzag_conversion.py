#!/usr/bin/env python3


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # print("convert: %s" % s)
        
        if len(s) <= numRows:
            return s
        
        if numRows == 1:
            return s

        ans = ""
        ans += s[::2*(numRows - 1)]
        # print("head:%s" % ans)
        for i in range(1, numRows - 1):
            ans += self.get_zigzag(i, s, numRows)
        ans += s[numRows-1::2*(numRows - 1)]
        # print("tail:%s" % s[numRows-1::2*(numRows - 1)])
        return ans

    @staticmethod
    def get_zigzag(index, s, rows):
        end = len(s) - 1
        zigzag = ""
        p = index
        while True:
            zigzag += s[p]

            p += 2 * (rows - index - 1)
            if p > end:
                break
            zigzag += s[p]

            p += 2 * index
            if p > end:
                break
        # print("%u: %s" % (index, zigzag))
        return zigzag


if __name__ == "__main__":
    sol = Solution()
    ans = sol.convert("PAYPALISHIRING", 4)
    print(ans)
