class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        l = []
        max_len = 0
        for i, c in enumerate(s):
            
            if c in h:
                substr = s[h[c]+1:]
                # print(substr)
                length = self.lengthOfLongestSubstring(substr)
                l.clear()
            else:
                h[c] = i
                l.append(c)
                # print(l)
                length = len(l)
            if length > max_len:
                max_len = length
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




