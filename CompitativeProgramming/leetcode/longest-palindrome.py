class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count=Counter(s)

        numberOfcount1=1
        countLength=0
        for key in count:
            if count[key]%2==0:
                countLength+=count[key]
            elif count[key]>1:
                countLength+=(count[key]-1)
                if numberOfcount1:
                    countLength+=1
                    numberOfcount1-=1
            elif count[key]==1 and numberOfcount1!=0:
                countLength+=1
                numberOfcount1-=1
        return countLength


        
        