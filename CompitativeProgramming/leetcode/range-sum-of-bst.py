# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      
 
        return self.rangeHelper(root,low,high)


    

    def rangeHelper(self,root,low,high):
        if not root:
            return 0
        
        if root.val>=low and root.val<=high:
            return root.val+self.rangeHelper(root.left,low,high)+self.rangeHelper(root.right,low,high)
        else:
            return self.rangeHelper(root.left,low,high)+self.rangeHelper(root.right,low,high)
       

            


        