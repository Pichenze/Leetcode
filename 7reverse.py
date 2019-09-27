class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        if x < 0:
            sig = -1
            x = -x
        else:
            sig = 1
        while x:
            num += x%10
            num *= 10
            x = x//10
        num =sig*(num//10)
        # 边界条件
        v_max = 0xffffffff/2
        if num > (v_max -1) or num < (v_max*(-1)):
            return 0
        return num
