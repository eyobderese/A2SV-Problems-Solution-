class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        stack=[]

        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')' and stack:
                stack.pop()
            elif i==')' and not stack:
                count+=1
        return count+len(stack)
            
