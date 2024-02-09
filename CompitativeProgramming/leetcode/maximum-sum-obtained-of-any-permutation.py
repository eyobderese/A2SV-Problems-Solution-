class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        Modd= pow(10,9)+7
        pre=[0 for i in range(n)]
        prefix=[]
        nums.sort()

        for st,end in requests:
            pre[st]+=1
            if end+1<n:
                pre[end+1]-=1
        total=0
        for i in pre:
            total+=i
            prefix.append(total)
        summ=0
        # prefix.pop()
        prefix.sort()
        

        print(prefix)
        print(nums)
        
        

        for j in range(len(nums)):
            summ+=prefix[j]*nums[j]
    
        return summ%Modd

        
       
        

        
       

        