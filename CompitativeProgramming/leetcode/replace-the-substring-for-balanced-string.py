class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance=len(s)/4
        counter=0
        store = defaultdict(int)
        tracker = defaultdict(int)
        ans=float('inf')
        flag=True
        for i in s:
            store[i]+=1
        left=0
        for right in range(len(s)):

            store[s[right]]-=1
            
            while store["W"]<= balance and store["Q"]<=balance and store["E"]<=balance and store["R"]<=balance:
                flag= False
                ans=min(right-left+1,ans)
                if left>right:
                    break
                store[s[left]]+=1
                left+=1
        return 0 if flag else ans 
            



       
               
           
            

            

        return 0 if flag else ans

       



        