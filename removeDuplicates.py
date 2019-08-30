class Solution:
	def removeDuplicates(self, nums):
		if len(nums)==0 or nums is None:
			return 0
		tmp = nums[0]
		leng = 1
		for i in range(1,len(nums)):
			if nums[i] != tmp:
				nums[leng] = nums[i]
				tmp = nums[leng]
				leng += 1
		nums[leng:] = []
		return leng
