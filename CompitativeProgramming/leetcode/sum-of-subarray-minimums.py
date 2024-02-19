class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
      
        stack=[]
        MOOD=10**9 + 7
        res=0

        for i in range(len(arr)):

            while stack and stack[-1][1]>arr[i]:
                j,val=stack.pop()
                right= i-j
                if stack:
                    left=j-stack[-1][0]
                else:
                    left=j+1
                res= (res+right*left*val)%MOOD
            stack.append((i,arr[i]))
        for i in range(len(stack)):
            j,val=stack[i]
            left=j-stack[i-1][0] if i>0 else j+1
            right=len(arr)-j
            
            res=(res+right*left*val)%MOOD
        
        return res



            








# [6,9,10,1,2,3 4 5 1]