# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        big=float('-inf')
        small=float("inf")
        
        return self.maxHelper(root,big,small)
        
    

    def maxHelper(self,root,big,small):
        
        if not root:
            return big-small
        big=max(big,root.val)
        small=min(small,root.val)

        left=self.maxHelper(root.left,big,small)
        right=self.maxHelper(root.right,big,small)
        return max(left,right)


        
        
       
        
       



    


        

 

        