#
# 1. 用递归可以解决问题, 递归的思路是:
#   a. 从字符串开始累加长度, 如果出现重复的字符,那么最长的substr 应该是剩下字符串中的 最长 substr 和当前最长 substr中的较长者.
#
# 2. 用滑动窗口的方法解决思路:
#   a. 在wind保存最长的substr.
#   b. 在h保存所有出现国的字符.
#   c. 如果出现重复的字符c，则将窗口缩小到c之后,同时也将缩小的窗口中的字符从h里面删除掉.
#


class Solution:
    
    def lengthOfLongestSubstringRecursion(self, s: str) -> int:
        h = {}
        max_len = 0
        for i, c in enumerate(s):
            
            if c in h:
                substr = s[h[c]+1:]
                length = self.lengthOfLongestSubstringRecursion(substr)

                if length > max_len:
                    max_len = length
                return max_len
            else:
                h[c] = i
                max_len += 1
        return max_len

    def lengthOfLongestSubstringWindows(self, s: str) -> int:
        
        h = {}
        wind = []
        max_len = 0
        
        for i, c in enumerate(s):
            if c in h:
                p = ""
                while p != c:
                    p = wind.pop(0)
                    del h[p]
            wind.append(c)
            h[c] = i
            
            wind_size = len(wind)
            
            if wind_size > max_len:
                max_len = wind_size
                
        return max_len
        

if __name__ == '__main__':
    sol = Solution()
    ans = sol.lengthOfLongestSubstringWindows("bbbbb")
    print(ans)
    ans = sol.lengthOfLongestSubstringWindows("abcabcbb")
    print(ans)
    ans = sol.lengthOfLongestSubstringWindows("dvdf")
    print(ans)
    ans = sol.lengthOfLongestSubstringWindows("pwwkew")
    print(ans)
    ans = sol.lengthOfLongestSubstringWindows("ckilbkd")
    print(ans)
    ans = sol.lengthOfLongestSubstringWindows("klvqkpqivdcrpgkcttmkrgtekiclinf")
    print(ans)




