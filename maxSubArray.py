class Solution:
# 动态规划 ： 用sums保存以第i个数字为结尾的最大子序列和
	def maxSubArray(self, nums):
		maxsum = nums[0]
		sums = nums[0]
		for i in range(1,len(nums)):
			# sums用于表示以第i-1个数字为结尾子序列的最大和
			if sums < 0: #也就是说 sums + nums[i] < nums[i] , 因此第i个数字为结尾子序列的最大和一定是nums[i]本身
				sums = nums[i]
			else:  #也就是说 sums + nums[i] >= nums[i] , 因此第i个数字为结尾子序列的最大和一定是nums[i]+sums
				sums += nums[i]
			if sums >= maxsum:
				maxsum = sums
		return maxsum
