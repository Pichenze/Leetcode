class Solution:
	def sortList(self, head):
		node = head
		nums = []
		while node:
			nums.append(node.val)
			node = node.next
		nums = sorted(nums)
		head = createlist(nums)
		return head

#创建链表
def createlist(lists:list):
	head = point = ListNode(0)
	for i in lists:
		point.next = ListNode(i)
		point = point.next
	return head.next
