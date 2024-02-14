class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change=defaultdict(int)
        for i in bills:
            if i==5:
                change[i]+=1
            elif i==10 and change[5]>0:
                change[i]+=1
                change[5]-=1
            elif i==20 and (change[10]>0 and change[5]>0):
                change[i]+=1
                change[5]-=1
                change[10]-=1
            elif i==20 and change[5]>2:
                change[i]+=1
                change[5]-=3
            else:
                return False
        return True




        