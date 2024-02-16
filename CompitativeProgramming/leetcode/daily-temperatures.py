class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack=[]
        mapp={}
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                mapp[stack[-1]]=(i-stack[-1])
                stack.pop()
            stack.append(i)
        ans=[0]*len(temperatures)

        for key in mapp:
            ans[key]=mapp[key]
        return ans 



