# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tracker=deque([root] if root else [])

        
        out=[]
        while tracker:
            level=[]

            for i in range(len(tracker)):
                node =tracker.popleft()
                level.append(node.val)
                if node.left:
                    tracker.append(node.left)
                if node.right:
                    tracker.append(node.right)
            out.append(level)
        
        for i in range(len(out)):
            if i%2==1:
                out[i]=reversed(out[i])
        return out


        