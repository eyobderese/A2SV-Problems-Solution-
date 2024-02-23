# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        store=[]
        store =self.validateHelper(root,store)
        
        return store==sorted(store) and len(set(store))==len(store)

    

    def validateHelper(self,root,store):
        if not root:
            return 
        self.validateHelper(root.left,store)
        store.append(root.val)
        self.validateHelper(root.right,store)
        return store




        
        
        

        