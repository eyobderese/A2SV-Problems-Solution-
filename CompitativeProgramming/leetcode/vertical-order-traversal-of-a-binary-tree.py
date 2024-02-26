# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        tracker=defaultdict(list)
        index=0
        def helper(root,x,y):
            nonlocal tracker
            if not root:
                return 
            
            tracker[x].append((y,root.val))
            helper(root.left,x-1,y+1)
            helper(root.right,x+1,y+1)
        helper(root,index,0)

        keys=sorted(tracker.keys())
        ans=[]
        for key in keys:
            contant=tracker[key]
            contant.sort()
            temp=[]
            for index,val in contant:
                temp.append(val)
            ans.append(temp)

        # print(ans)
        return ans
       
        

        