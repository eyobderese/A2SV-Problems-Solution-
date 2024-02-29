# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        tracker=defaultdict(list)
        def helper(root,x,y):
            nonlocal tracker
            if not root:
                return
              
            tracker[y].append(x)
            helper(root.left,2*x-1,y+1)
            helper(root.right,2*x,y+1)
        helper(root,1,0)
        ans=float("-inf")
        for key in tracker:
            currAns=max(tracker[key])-min(tracker[key])+1
            ans=max(ans,currAns)
        return ans
    


        