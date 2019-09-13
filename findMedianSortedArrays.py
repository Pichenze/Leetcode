class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		m,n = len(nums1),len(nums2)
		# 固定 m <= n,nums1比nums2小
		if m > n:
			nums1,nums2 = nums2,nums1
			m,n = n,m

		iMin,iMax,halfLen = 0,m,(m+n+1)//2
		# 在 nums1 中找到整体的中位数在nums1的索引位置
		# i , j 分别用于寻找 nums1 和 nums2 中的整体索引
		# 找到i 和 j 使得 i + j == halflen(也就是前面有一半个数，这样的话就可以找到中位数的位置了)
		while iMin <= iMax:
			i = (iMin + iMax)//2 
			j = halfLen - i
			if i < iMax and nums2[j-1] > nums1[i]:
				iMin = i + 1  # i is too small
			elif i > iMin and nums1[i-1] > nums2[j]:
				iMax = i-1  # i is too big
			else:  # i is perfect
				maxleft = 0
				if i == 0:
					maxleft = nums2[j-1]
				elif j == 0:
					maxleft = nums1[i-1]
				else:
					maxleft = max(nums1[i-1],nums2[j-1])
				# 总共有 奇数个数，中位数就是中间那个	
				if (m+n)%2 == 1:
					return maxleft

				# 总有 偶数个数，中位数就是中间两个的均值
				minright = 0
				if i == m:
					minright = nums2[j]
				elif j == n:
					minright = nums1[i]
				else:
					minright = min(nums2[j],nums1[i])

				return (maxleft + minright)/2.0
		return 0.0
