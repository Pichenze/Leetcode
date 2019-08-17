class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# 递归中的函数调用是自顶向下的过程，函数参数可以往下传递。使用return可以实现指标自底向上传递，前提是采用的是后序遍历，也就是左孩子->右孩子->根节点的顺序遍历，这样就可以把孩子结点的信息自底向上传递。
	# 这里return返回的指标是以该节点为根自顶向下找到一条路径（也就是要嘛跟左孩子连接要嘛根右孩子连接或是不连接三种情况）使得路径和最大
  # 注意，curse_tree(node)返回的是从node结点自顶向下的最大路径和，如对树[0,1,2,3,4,5,6]
		'''
			0
		   / \
		  1   2
		 / \  / \
		3  4 5  6
		
		3,4,5,6是叶节点，所以在遍历这几个节点时，返回的值是本身，
		而对1结点，返回的时1 + max(0,3,4)  0表示两个孩子结点都是负数，加上它们的话只会使包含1结点的路径更小，干脆不要
		对2结点，返回的是2+max(0,5,6)
		对0结点，返回的使0 + max(0,1 + max(0,3,4),2+max(0,5,6))
		也就是对node:
		     返回 node.val + max(0,node.left.val,node.right.val)
		返回的只是一条自顶向下的最大路径和，但是可以帮助计算从树的任一个结点到另一个节点的路径和（树的路径是由根连接起来的）
		
		'''
	def maxPathSum(self, root: TreeNode) -> int:
		self.maxpathsum = -1e50  #保存最大路径值		
		def curse_tree(node):  #树的后序遍历
			#print('It\'s node ',node.val)
			if node.left is None and node.right is None: # 处理 叶节点
				self.maxpathsum = max(self.maxpathsum,node.val) 
				#print(self.maxPathSum)
				return node.val
			leftsum = 0
			rightsum = 0
			if node.left:
				leftsum = curse_tree(node.left)
			if node.right:
				rightsum = curse_tree(node.right)

			self.maxpathsum = max(self.maxpathsum,node.val+max(0,leftsum)+max(0,rightsum)) #有如果leftsum<0说明有左分支不如没有，同理右分支也一个意思
			#print(self.maxPathSum)
			return node.val+max(0,leftsum,rightsum)  #以node为出发点，向后代行走的一条最大值路径
		curse_tree(root)
		#print('Hello',self.maxpathsum)
		return self.maxpathsum
