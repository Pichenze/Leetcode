class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if head is None or head.next is None:
			return head
		node = head
		length = 0
		# 遍历一次得到链表长度，和链表尾结点
		while node:
			length += 1
			if node.next is None:
				tail = node
			node = node.next
		prenode = node = head

		print('tail val:',tail.val,'  length : ',length)
		# 旋转 length倍数次的话链表不变
		if k%length == 0:
			return head

		# 找到新的头节点newhead和新的尾结点prenode(它们的关系是新的尾结点的next是新的头节点)
		for i in range(length - (k%length)):
			prenode = node
			node = node.next
		#print('prenode : {0}  node:{1}'.format(prenode.val,node.val))
		newhead = node
		tail.next = head
		prenode.next = None
		return newhead
