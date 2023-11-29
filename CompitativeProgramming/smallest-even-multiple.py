class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        m=n
        while True:
            if m%2==0 and m%n==0:
                return m
            else:
                m+=1

        
        