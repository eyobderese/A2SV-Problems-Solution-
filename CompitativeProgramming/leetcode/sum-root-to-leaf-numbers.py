# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        store=[]
        ans=0
        def helper(root,ans):
            nonlocal store
            ans=ans*10
            ans+=root.val
            if not root.left and not root.right:
                store.append(ans)
                return 
            elif not root.left:
                helper(root.right,ans)
                return 
            elif not root.right:
                helper(root.left,ans)
                return 

            else:
                helper(root.left,ans)
                helper(root.right,ans)

        helper(root,ans)
       
        return sum(store)



        