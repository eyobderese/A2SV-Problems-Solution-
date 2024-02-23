# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        dummyNode=TreeNode(0)

        self.mergeHelper(root1,root2,dummyNode)

        return dummyNode if root1 or root2 else None
    

    def mergeHelper(self,root1,root2,dummy):


        if root1 and root2:
            dummy.val=root1.val+root2.val

            if root1.left or root2.left:
                dummy.left=TreeNode(0)
                self.mergeHelper(root1.left,root2.left,dummy.left)
            if root1.right or root2.right:
                dummy.right=TreeNode(0)
                self.mergeHelper(root1.right,root2.right,dummy.right)



        elif root1:
            dummy.val=root1.val
            if root1.left:
                dummy.left=TreeNode(0)
                self.mergeHelper(root1.left,None,dummy.left)    
            if root1.right:
                dummy.right=TreeNode(0)
                self.mergeHelper(root1.right,None,dummy.right)

        elif root2:
            dummy.val=root2.val

            if root2.left:
                dummy.left=TreeNode(0)
                self.mergeHelper(None,root2.left,dummy.left)
            if root2.right:
                dummy.right=TreeNode(0)
                self.mergeHelper(None,root2.right,dummy.right)
        else:
            dummy=None
           




        