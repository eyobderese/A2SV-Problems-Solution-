class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        arry=list(map(int,list(s)))

        pre01=[]
        pre10=[]
        N_0=0
        N_1=0
        summ=0
        summ1=0
        for i in range(len(arry)):
            if arry[i]==0:
                summ1+=N_1
                N_0+=1
                pre01.append(summ)
                pre10.append(summ1)
            else:
                summ+=N_0
                pre01.append(summ)
                N_1+=1
                pre10.append(summ1)
        count=0

        for i in range(len(arry)):
            if arry[i]==0:
                count+=pre01[i]
            else:
                count+=pre10[i]
        return count


        return 1




        