class Solution:
	def reverseList(self, head):
		prevnode = None
		node = head 
		while node:
			nextnode = node.next 
			node.next = prevnode
			prevnode = node
			node = nextnode
		return prevnode
