class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        re_x = list(reversed(x))
        
        for i in range(len(x)):
            if x[i] != re_x[i]:
                return False
            
        return True
