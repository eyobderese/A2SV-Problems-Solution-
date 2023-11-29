class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3!=0: return []
        starting_number=(num-3)//3
        return ([starting_number,starting_number+1,starting_number+2])
