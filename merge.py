class Solution:
	def merge(self, nums1, m, nums2, n):
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		if n == 0:
			return
		elif m == 0:
			nums1 = nums2[:n]
			#print(nums1)
			return
		tail = m+n-1
		i,j = m-1,n-1
		while tail >= 0:
			if nums1[i] < nums2[j]:
				nums1[tail] = nums2[j]
				tail -= 1
				j -= 1
			elif nums1[i] > nums2[j]:
				nums1[tail] = nums1[i]
				tail -= 1
				i -= 1
			else:
				nums1[tail],nums1[tail-1] = nums1[i],nums2[j]
				tail -= 2
				i -= 1
				j -= 1

			if i == -1:
				while j > 0:
					nums1[tail] = nums2[j]
					tail -= 1
					j -= 1
				break
			if j == -1:
				break
		print(nums1)
