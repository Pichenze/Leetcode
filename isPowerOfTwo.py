class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0
    
# 2的幂次在二进制表示即是只有一位为1其余位都是0，而2的幂次-1的数字的二进制数字表示则全部都是1且位数少一位，因此两数相与得到的数字正好是0
