# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store=[]
        store=self.helper(root,store)
        return store[k-1]

    

    def helper(self,root,store):
        if not root:
            return 
        self.helper(root.left,store)
        store.append(root.val)
        self.helper(root.right,store)
        return store

        