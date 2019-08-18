class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = []
        def curse_tree(node):
            left,right = 0,0
            if node.left:
                left = curse_tree(node.left)
            if node.right:
                right = curse_tree(node.right)
            if node==p or node==q:
                if left+right==1:
                    lca.append(node)
                    return 0
                else:
                    return 1 
            if left+right == 2:
                lca.append(node)
                return 0
            else:
                return left+right
        curse_tree(root)
        print(lca)
        if len(lca)==0:
            return None
        return lca[0]
