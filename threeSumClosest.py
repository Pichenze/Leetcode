class Solution:
	# 双指针法：固定最小值，后边的区域用双指针start,end来向结果逼近
	def threeSumClosest(self, nums, target):
		close_num = 1e10
		nums = sorted(nums)
		low,high = 0,len(nums)-1
		for i in range(0,len(nums)-2):
			start,end = i+1,len(nums)-1 
			while start<end:
				if nums[i]+nums[start]+nums[end] == target:
					return target
				elif nums[i]+nums[start]+nums[end] < target:
					if abs(close_num-target) > target - (nums[i]+nums[start]+nums[end]):
						close_num = nums[i]+nums[start]+nums[end]
					start += 1 
				elif nums[i]+nums[start]+nums[end] > target:
					if abs(close_num-target) > (nums[i]+nums[start]+nums[end])-target:
						close_num = nums[i]+nums[start]+nums[end]
					end -= 1
		return close_num
