class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	
	# 1、将链表直接合并，然后直接排序
    def mergeKLists_1(self, lists):
    	self.nodes = []
    	head = point = ListNode(0)
    	for l in lists:
    		while l:
    			self.nodes.append(l.val)
    			l = l.next
    	for x in sorted(self.nodes):
    		point.next = ListNode(x)
    		point = point.next
    	return head.next

    #2、优先队列PriorityQueue优化(优先队列put操作会默认按照值的大小插入使队列有序，get则是获得值最小得元素)
	def mergeKLists_2(self, lists):
		from queue import PriorityQueue
		head = point = ListNode(0)
		q = PriorityQueue()
		for l in lists:
			if l:
				q.put((l.val,l))
		while not q.empty():
			val,node = q.get()
			point.next = ListNode(val)
			point = point.next
			node = node.next
			if node:
				q.put((node.val,node))
		return head.next
	
	#3、分治（核心：interval的动态变化，以及在数组中的应用）
	def mergeKLists(self, lists):
		amount = len(lists)
		if amount == 0:
			return None
		interval = 1  #要合并的两个链表在列表中的索引间距
		while interval<amount: #合并链表的结束条件
			for i in range(0,amount-interval,2*interval): # 合并 lists[i]和lists[i+interval]
				lists[i] = self.merge2Lists(lists[i],lists[i+interval])
			interval *= 2 #一次合并后，interval*2
		return lists[0] if amount > 0 else lists

	def merge2Lists(self,l1,l2):
		head = point = ListNode(0)
		while l1 and l2:
			if l1.val <= l2.val:
				point.next = l1
				l1 = l1.next
			else:
				point.next = l2
				l2 = l2.next
			point = point.next
		if l1:
			point.next = l1
		if l2:
			point.next = l2
		return head.next
