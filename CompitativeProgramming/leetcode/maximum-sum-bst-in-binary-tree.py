# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        
        maxSum=0
        
        

        def helper(root):
            # print(root.val)
            nonlocal maxSum
            if not root:
                return (0,float('inf'),float("-inf"))



            summLeft, minLeft,maxLeft=helper(root.left)
            summRight,minRight,maxRight=helper(root.right)

            
            


            if summLeft != None and  summRight!=None:        
                if maxLeft>=root.val:
                    return None,None,None                
                if minRight<=root.val:
                    return None,None,None
                minVal=min(root.val,minLeft)
                maxVal=max(root.val,maxRight)

                maxSum=max(maxSum,root.val+summLeft+summRight)

                return root.val+summLeft+summRight,minVal,maxVal
            return None,None,None


        helper(root)
        return maxSum

            

        