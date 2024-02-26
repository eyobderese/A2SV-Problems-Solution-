# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        store=[]
        def helper(root):
            nonlocal store
            if not root:
                return 
            
            helper(root.left)
            store.append(root.val)
            helper(root.right)
        helper(root)

        count = Counter(store)
        tracker=defaultdict(list)
        maxx=float('-inf')
        for key in count:
            tracker[count[key]].append(key)
            maxx=max(count[key],maxx)
        return tracker[maxx]




        
        
        
        return store
        