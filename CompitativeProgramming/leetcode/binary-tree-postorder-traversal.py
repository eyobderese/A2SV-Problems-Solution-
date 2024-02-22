# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.postHelper(root,ans)
        return ans
    
    def postHelper(self,root,ans):
        if not root:
            return 
        self.postHelper(root.left,ans)
        self.postHelper(root.right,ans)
        ans.append(root.val)
        
