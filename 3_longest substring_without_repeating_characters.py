class Solution:
    max_len = 0
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        for i, c in enumerate(s):
            
            if c in h:
                substr = s[h[c]+1:]
                print(substr)
                length = self.lengthOfLongestSubstring(substr)
            else:
                h[c] = i
                length = ?
            if length > self.max_len:
                self.max_len = length
        return self.max_len


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
    ans = sol.lengthOfLongestSubstring("ckilbkd")
    print(ans)


