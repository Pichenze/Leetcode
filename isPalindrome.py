class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = 0
        tmp = x
        while tmp:
            num *= 10
            num += tmp%10
            tmp = tmp//10
        if num == x:
            return True
        return False
