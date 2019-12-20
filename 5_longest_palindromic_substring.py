#!/usr/bin/env python3


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1:
            return s
        longest = ""
        print("check:", s)

        for pos in range(1, length):
            # res = self.check_odd(pos, s)
            # if len(res) > len(longest):
            #     longest = str(res)

            res = self.check_even(pos, s)
            if len(res) > len(longest):
                longest = str(res)

        return longest

    @staticmethod
    def check_odd(pos, s):

        if pos == len(s) - 1:
            return ""

        offset = 1
        while True:

            if s[pos - offset] != s[pos + offset]:
                return s[pos - offset + 1 : pos + offset]

            if pos - offset - 1 < 0 or pos + offset + 1 > len(s) - 1:
                break

            offset += 1

        return s[pos - offset : pos + offset + 1]

    @staticmethod
    def check_even(pos, s):
        offset = 0
        print("check even: pos:%u" % pos)
        while True:

            if s[pos - offset - 1] != s[pos + offset]:
                return s[pos - offset : pos + offset]

            if (pos - offset - 1) < 0 or (pos + offset) > len(s) - 1:
                print(
                    "OUT! pos:%u offset:%u %s vs %s"
                    % (pos, offset, (pos - offset - 1), (pos + offset))
                )
                break

            offset += 1

        return s[pos - offset : pos + offset]


if __name__ == "__main__":
    sol = Solution()
    ts = "aaaa"
    ans = sol.longestPalindrome(ts)
    print("final:", ans)
