class Solution:
    def maxDepth(self,root: TreeNode):
    	self.maxdepth = 0
    	def curse_tree(depth,node):
    		if depth>self.maxdepth: #比较最大深度
    			self.maxdepth = depth
    		if node.left:  # node有左孩子
    			curse_tree(depth+1,node.left)
    		if node.right:  # node有右孩子
    			curse_tree(depth+1,node.right)
    		return
    	if root == None:
    		return 0
    	curse_tree(1,root)
    	return self.maxdepth
