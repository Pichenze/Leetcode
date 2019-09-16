class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		head = node = ListNode(0)
		while l1 and l2:
			if l1.val < l2.val:
				node.next = ListNode(l1.val)
				node = node.next
				l1 = l1.next
			elif l1.val > l2.val:
				node.next = ListNode(l2.val)
				node = node.next
				l2 = l2.next
			else:
				node.next = ListNode(l1.val)
				node.next.next = ListNode(l2.val)
				node = node.next.next
				l1 = l1.next
				l2 = l2.next
		if l1:
			node.next = l1
		if l2:
			node.next = l2
		return head.next
