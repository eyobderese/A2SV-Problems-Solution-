class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        pref=[0]*(n+2)
        for strt,end,reserv in bookings:
            pref[strt]+=reserv
            pref[end+1]-=reserv
        
        ans=[]
        summ=0
        for i in pref:
            summ+=i
            ans.append(summ)
        return ans[1:len(ans)-1]
        