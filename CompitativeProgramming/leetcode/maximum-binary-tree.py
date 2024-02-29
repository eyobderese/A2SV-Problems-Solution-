# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        def helper(nums):

            if len(nums)==1:
                return TreeNode(nums[0])
            if len(nums)==0:
                return None
            
            maxx=max(nums)
        
            i=nums.index(maxx)
            Node1=TreeNode(maxx)
            Node1.left=helper(nums[:i])
            Node1.right=helper(nums[i+1:])

            return Node1
       
        return helper(nums)
            
                    
        