class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        for i in nums:
            if str(i) in mydict:
                mydict[str(i)] += 1
            else:
                mydict[str(i)] = 1
            if mydict[str(i)] > len(nums)//2:
                    return i
