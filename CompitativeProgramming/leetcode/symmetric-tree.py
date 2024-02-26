# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(right,left):
            if not right and not left:
                return True
            elif not right:
                return False
            elif not left:
                return False
            elif right.val!=left.val:
                return False
            
            val1=helper(right.left,left.right)
            val2=helper(right.right,left.left)
            return val1 and val2

        return helper(root.left,root.right)
            
        
     
            
            
            


        