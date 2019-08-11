class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        def trackback(i,tmp):  #回溯算法，递归，dfs
            res.append(tmp)
            for j in range(i,n):
                trackback(j+1,tmp+[nums[j]])
        trackback(0,[])
        return res

    
class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = [[]]
        for i in range(n): #迭代算法，闭包,bfs
            res += [[nums[i]]+num for num in res]
        return res
