class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = []
        # 二叉树的后序遍历，自底向上传递值（return返回的值是对结点node它的孩子中（包含本身）有[p,q]中的几个）
        def curse_tree(node):
            left,right = 0,0  # 初始化left,right为0
            if node.left:   # node有左孩子，在左孩子寻找是否有p,q
                left = curse_tree(node.left)   # 左孩子，返回的左孩子底下的是p,q总个数
            if node.right:  # node有右孩子，在右孩子寻找是否有p,q
                right = curse_tree(node.right)  # 右孩子

            # 根节点
            if node==p or node==q:  #当前结点node是p或是q
                if left+right==1:  #如果node的左孩子或是右孩子中存在一个p或q,那么就说明node就是最近共同祖先
                    lca.append(node)
                    return 0
                else:  # 当前结点为p或q,则返回1，表示找到p或q中的一个了
                    return 1 
            if left+right == 2: # left+right==2表示在左孩子和右孩子中找到了p或q各一个，总共两个了
                lca.append(node)
                return 0
            else:
                return left+right
        curse_tree(root)
        print(lca)
        if len(lca)==0:
            return None
        return lca[0]
