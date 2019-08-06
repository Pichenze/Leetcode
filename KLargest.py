class Solution:
	# 1、考虑k与n/2的关系进行最大或最小排序的冒泡排序
	def findKthLargest_1(self, nums, k: int) -> int:
		n = len(nums)
		if k <= n/2:
			for epoch in range(k):
				for i in range(n-1-epoch):
					if nums[i] > nums[i+1]:
						tmp = nums[i]
						nums[i] = nums[i+1]
						nums[i+1] = tmp
			return nums[-k]
		else:
			for epoch in range(n+1-k):
				for i in range(n-1-epoch):
					if nums[i] < nums[i+1]:
						tmp = nums[i]
						nums[i] = nums[i+1]
						nums[i+1] = tmp
			return nums[k-n-1]


	# 2、堆排序 超出时间限制
	def findKthLargest_2(self, nums, k: int) -> int:
		n = len(nums)
		for i in range(n,k,-1):
			nums = self.heap_bottom_up(nums,i)
			#print(i,' before : ',nums)
			tmp = nums[i-1]
			nums[i-1] = nums[0]
			nums[0] = tmp
			#print(i,' after : ',nums)
		nums = self.heap_bottom_up(nums,k)
		#print(nums)
		return nums[0]
    
    # 堆的 自底向上和自顶向下调整的选择： 
    # 建堆 ：一次自底向上调整（得到正确的堆顶元素），多次自顶向下知道满足堆的条件
    # 假设堆已经建好的情况下，如果变动的是堆顶，则采用自顶向下调整，如果变动的是堆底，则采用自底向上调整
	# 自底向上调整 往堆中插入新元素（一般是放在堆最末）适合的调整
	def heap_bottom_up(self,nums,k):  # 堆大小为k个元素，nums存放堆的元素
		while True:
			cnt = 0
			for i in range(k-1,0,-1):
				parent = (i-1)//2
				if nums[i] < nums[parent]:  # 当前结点值 是否小于双亲结点   在堆中，如果一个结点索引为i,有双亲结点，则其双亲结点索引为（i-1）//2
					tmp = nums[i]
					nums[i] = nums[parent]
					nums[parent] = tmp
					cnt += 1
			if cnt==0:
				break
			#print('you :',nums)
			
		return nums	

	# 自顶向上 堆调整（在建完堆的前提下，将堆顶最小元素与堆最后的元素替换后的调整），删除堆顶元素之后做的调整
	def heap_top_down(self,nums,k): # 堆大小为k个元素，nums存放堆的元素
		for i in range(0,k):
			if 2*i+2 < k: # i有左孩子且有右孩子
				if nums[2*i+2] <=nums[2*i+1] and nums[2*i+2]<nums[i]:
					tmp = nums[2*i+2]
					nums[2*i+2] = nums[i]
					nums[i] = tmp
				elif nums[2*i+1] <nums[2*i+2] and nums[2*i+1]<nums[i]:
					tmp = nums[2*i+1]
					nums[2*i+1] = nums[i]
					nums[i] = tmp
			elif 2*i+1 < k:
				if nums[2*i+1]<nums[i]:
					tmp = nums[2*i+1]
					nums[2*i+1] = nums[i]
					nums[i] = tmp
		#print('hello : ',nums)
		return nums

	# 3、（推荐）建一个大小为k的最小堆，首先进行建堆，然后对第i (i = k+1：n)的元素与堆顶元素比大小，
	# 如果堆顶元素比第i个元素大的话（说明第i个元素一定是小于第k大的数的,不考虑），
	# 否则将堆顶元素与第i个元素进行替换（因为堆顶元素小于堆中的k-1个元素，并且小于第i个元素，所以一定小于第K大的元素），然后进行堆调整
	def findKthLargest(self, nums, k: int) -> int:
		n = len(nums)
		nums = self.heap_bottom_up(nums,k)
		for i in range(k,n):
			if nums[i] >= nums[0]:
				tmp = nums[i]
				nums[i] = nums[0]
				nums[0] = tmp
				nums = self.heap_top_down(nums,k)
		print(nums)
		return nums[0]

	# 4、heapq自带方法：
    def findKthLargest_4(self, nums, k):
        return heapq.nlargest(k, nums)[-1]



if __name__ == '__main__':
	nums = [2,8,6,7,3,5,4,9]
	nums1 = [3,2,1,5,6,4]
	nums2 = [3,2,3,1,2,4,5,5,6]
	solu = Solution()
	#solu.heap_top_down(nums,6)
	solu.findKthLargest(nums,6)
	solu.findKthLargest(nums1,2)
	solu.findKthLargest(nums2,4)
	#solu.findKthLargest_1(nums,6)

