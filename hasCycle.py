class Solution:
	def hasCycle(self, head):
		# 随便指定一个不可能出现的数值1e50,创建新的节点end，把所有遍历过的结点的next指向end,当遍历过程中node.next的值有1e10说明出现环了，否则遍历结束说明无环
		end = ListNode(1e10)
		node = head
		while node:
			if node.val == 1e10: # 遇到环了
				return True
			prenode = node 
			node = node.next
			prenode.next = end  # 把遍历过的结点都指向end结点
		return False
