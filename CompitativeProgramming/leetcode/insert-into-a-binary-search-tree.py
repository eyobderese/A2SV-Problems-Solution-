# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root=TreeNode(val)
            return root
        self.insertHelper(root,val)
        return root
    def insertHelper(self,root,val):

        if root.val>val and not root.left:
            root.left=TreeNode(val)
            return
        if root.val<val and not root.right:
            root.right=TreeNode(val)
            return 
        if root.val>val:
            self.insertHelper(root.left,val)
        else:
            self.insertHelper(root.right,val)


    

        