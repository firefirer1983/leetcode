class Solution:
    def myAtoi(self, str: str) -> int:
        negative = False
        num = 0
        for c in str:
            
            if ord(c) == ord(" "):
                continue
            
            if ord(c) == ord("-"):
                negative = True
                continue
            
            if ord(c) == ord("+"):
                continue
            
            if ord(c) < ord("0") or ord(c) > ord("9"):
                break
                
            num *= 10
            
            tmp = ord(c) - ord("0")
            num += tmp
        
        if negative:
            num = -1 * num
        
        if num >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num
        



if __name__ == "__main__":
    sol = Solution()
    tst = "4193 with words"
    ans = sol.myAtoi(tst)
    print(ans)
