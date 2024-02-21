class Solution:
    def trap(self, height: List[int]) -> int:
        tracker={}
        tracker2={}
        maxx=0
        for i in range(len(height)):
            tracker[i]=maxx
            maxx=max(maxx,height[i])
        
        maxx1=0
        for i in range(len(height)-1,-1,-1):
            tracker2[i]=maxx1
            maxx1=max(maxx1,height[i])

        ans=0
        for i in range(len(height)):
            min_height=min(tracker[i],tracker2[i])
            min_height-=height[i]
            
            if min_height>0:
                ans+=min_height
        return ans


        











        
        

        






        

      


       









        
        