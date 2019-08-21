class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        elif n > 2:
            stair = [0,1,2]
            for i in range(3,n+1):
                stair.append(stair[i-1]+stair[i-2])
        return stair[n]
