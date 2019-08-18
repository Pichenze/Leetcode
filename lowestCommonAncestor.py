class Solution:
	#二叉搜索树的最近公共祖先：对p,q两个结点，p,q的最近公共祖先的val一定在p,q的val之间，也就是说假设p.val<q.val则p.val<=node.val<=q.val
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		node = root
		while node:
			if node.val>=p.val and node.val<=q.val or node.val<=p.val and node.val>=q.val:  #node.val介于p,q之间
				return node
			if p.val>node.val and q.val>node.val: #p,q都大于当前node,因此最近公共祖先应该在node的右侧
				node = node.right
			elif p.val<node.val and q.val<node.val: #p,q都小于当前node,因此最近公共祖先应该在node的左侧
				node = node.left
