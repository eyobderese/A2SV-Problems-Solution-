# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        tracker=set()

        self.lowestHelper(root,p,tracker)
        ans=None
        while curr!=q:
            if curr in tracker:
                ans=curr
            if curr.val>q.val:
                curr=curr.left
            else:
                curr=curr.right
        if curr in tracker:
            ans=curr
        return ans
        
            
    

    def lowestHelper(self,root,node1,tracker):
        curr=root
        while curr!=node1:
            tracker.add(curr)
            if curr.val>node1.val:
                curr=curr.left
            else:
                curr=curr.right
        tracker.add(curr)



        
        


        