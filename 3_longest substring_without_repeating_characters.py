class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        max_len = 0
        for i, c in enumerate(s):
            
            if c in h:
                substr = s[h[c]+1:]
                length = self.lengthOfLongestSubstring(substr)
                if length > max_len:
                    max_len = length
                return max_len
            else:
                h[c] = i
                max_len += 1
        return max_len


if __name__ == '__main__':
    sol = Solution()
    # ans = sol.lengthOfLongestSubstring("bbbbb")
    # print(ans)
    # ans = sol.lengthOfLongestSubstring("abcabcbb")
    # print(ans)
    # ans = sol.lengthOfLongestSubstring("dvdf")
    # print(ans)
    # ans = sol.lengthOfLongestSubstring("pwwkew")
    # print(ans)
    # ans = sol.lengthOfLongestSubstring("ckilbkd")
    # print(ans)
    ans = sol.lengthOfLongestSubstring("klvqkpqivdcrpgkcttmkrgtekiclinf")
    print(ans)




