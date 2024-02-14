class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        ans=0
        store=[]
        for i in range(len(costs)):
            store.append([costs[i][0]-costs[i][1],i])

        store=sorted(store,key=lambda x:x[0])

        for i in range(len(store)):

            if i>=len(store)/2:
                index=store[i][1]

                ans+=costs[index][1]
            else:
                index=store[i][1]

                ans+=costs[index][0]
        return ans

        