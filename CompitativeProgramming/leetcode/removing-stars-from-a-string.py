class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]

        for i in s:
            if i=="*" and stack:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        