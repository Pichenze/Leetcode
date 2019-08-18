class Solution:
  # 线索二叉树性质，左孩子结点<双亲结点<右孩子结点。
	# 对线索二叉树进行中序遍历（左根右）可以得到顺序递增的数,用列表存储就可以得到顺序递增的列表
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		nums = []  #用于保存线索二叉树的顺序列表表示
		def curse_tree(node):
			if node.left:
				curse_tree(node.left)
			nums.append(node.val)
			if node.right:
				curse_tree(node.right)
		curse_tree(root)
		return nums[k-1]
