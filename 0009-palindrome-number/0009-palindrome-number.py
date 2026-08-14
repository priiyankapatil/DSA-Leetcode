class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        reverse=0
        while x>0:
            rem=x%10
            reverse= reverse*10+rem
            x=x//10

        return original==reverse

        
    
