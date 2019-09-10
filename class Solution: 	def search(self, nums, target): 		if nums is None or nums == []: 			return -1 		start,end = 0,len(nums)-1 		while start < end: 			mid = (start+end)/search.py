class Solution:
	def search(self, nums, target):
		if nums is None or nums == []:
			return -1
		start,end = 0,len(nums)-1
		while start < end:
			mid = (start+end)//2
			print(start,mid,end)
			if nums[mid]==target:
				return mid
			# 利用了在 有序 较容易判断的特点简化了其他复杂情况
			if nums[start] <= nums[mid]:  #start-mid无旋转轴，start-mid是有序的（有序的话就容易判断target是否在start-mid中）
				if nums[start] <= target and target < nums[mid]: 
					end = mid - 1
				else:
					start = mid + 1
			else:  # 旋转轴在 start-mid之间，mid-end之间是有序的
				if target > nums[mid] and nums[end] >= target:
					start = mid + 1
				else:
					end = mid - 1
		if start > end:
			return -1
		else:
			if nums[start] == target:
				return start
			else:
				return -1
