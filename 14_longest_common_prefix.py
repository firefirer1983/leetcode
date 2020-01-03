#!/usr/bin/env python3


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        shortest_index = 0
        for i, s in enumerate(strs[1:]):
            if len(s) < len(strs[shortest_index]):
                shortest_index = i + 1

        shortest = strs[shortest_index]
        del strs[shortest_index]

        for i, c in enumerate(shortest):

            for s in strs:
                if s[i] != c:
                    return shortest[:i]

        return shortest


if __name__ == "__main__":
    sol = Solution()
    tst = ["flower", "flow", "flight"]
    ans = sol.longestCommonPrefix(tst)
    print(ans)
