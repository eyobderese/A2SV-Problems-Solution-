class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        count=0

        while target>1:

            if maxDoubles>0:
                if target%2==0:
                    count+=1
                    maxDoubles-=1
                    target=target//2
                else:
                    target-=1
                    count+=1
            else:
                return count+target-1
        return count



        