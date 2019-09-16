class Solution:
	def detectCycle(self, head):
		visited = set()
		node = head
		while node:
			if node in visited:
				print(node.val)
				return node
			else:
				visited.add(node)
				node = node.next
		return None
