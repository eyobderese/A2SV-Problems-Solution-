# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree=[]
        def helper(root):

            if not root:
                return 
            helper(root.left)
            tree.append(root.val)
            helper(root.right)
        
        def constructer(tree):
            if len(tree)==1:
                return TreeNode(tree[0])
            if len(tree)==0:
                return 
            mid=len(tree)//2
            Node=TreeNode(tree[mid])
            Node.left=constructer(tree[:mid])
            Node.right=constructer(tree[mid+1:])

            return Node
        helper(root)
        return constructer(tree)
        
        