#!/usr/bin/env python3


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        center = length / 2
        longest = ""
        longest_len = 0
        for pos in range(length):
            if pos < center:
                wing_size = len(s[:pos])
                odd_string = s[: pos + wing_size + 1]
                even_string = s[: pos + wing_size]
            else:
                wing_size = len(s[pos:])
                odd_string = s[pos - wing_size :]
                even_string = s[pos - wing_size :]

            odd_res = self.check_odd(odd_string)
            odd_len = len(odd_res)
            if odd_len > longest_len:
                longest, longest_len = odd_res, odd_len

            even_res = self.check_even(even_string)
            even_len = len(even_res)
            if even_len > longest_len:
                longest, longest_len = even_res, even_len

        return longest

    @staticmethod
    def check_odd(test_str):
        center = int(len(test_str) / 2)
        offset = 0
        while offset <= center:
            if test_str[center - offset] != test_str[center + offset]:
                offset -= 1
                return test_str[center - offset: center + offset]
            else:
                offset += 1
        return test_str
    
    @staticmethod
    def check_even(test_str):
        center = int(len(test_str) / 2)
        offset = 0
        while offset <= center:
            if test_str[center - offset] != test_str[center]:
                if offset == 0:
                    return ""
                else:
                    offset -= 1
                return test_str[center - offset: center + offset]
            else:
                offset += 1
        return test_str



if __name__ == "__main__":
    sol = Solution()
    ts = "aaaa"
    ans = sol.longestPalindrome(ts)
    print(ans)
