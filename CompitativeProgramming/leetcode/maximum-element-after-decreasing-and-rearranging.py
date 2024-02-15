class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int


        """
        count=defaultdict(int)
        m=len(arr)
        store=set(arr)
        surPlaus=0
        
        for i in arr:
            if i>m:
                surPlaus+=1
            else:
                count[i]+=1

        
        for i in range(m,0,-1):
            if i in store:
                surPlaus+=(count[i]-1)
                continue
            elif surPlaus>0:
                surPlaus-=1
            else:
                m-=1
        return m
                

        



        
       

       

        return arr[-1]