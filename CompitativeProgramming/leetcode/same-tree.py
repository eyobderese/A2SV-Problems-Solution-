# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(self.sameHelper(p,q))
        return self.sameHelper(p,q)

    


    def sameHelper(self,root1,root2):
        
        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        
        if root1.val==root2.val:
            val=self.sameHelper(root1.left,root2.left)
            val1=self.sameHelper(root1.right,root2.right)
            return val and val1
        if root1.val!=root2.val:
            return False

        

        