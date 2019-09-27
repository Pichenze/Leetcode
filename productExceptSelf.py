class Solution:
	def productExceptSelf(self, nums):
		res, l, r = [1] * len(nums), 1, 1
		#print('res : ',res)
		for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
			res[i], l = res[i] * l, l * nums[i]  # l 表示 i左边所有元素的乘积
			res[j], r = res[j] * r, r * nums[j]  # r 表示 i右边所有元素的乘积
			#print(i,j,l,r,'res : ',res)
		return res
