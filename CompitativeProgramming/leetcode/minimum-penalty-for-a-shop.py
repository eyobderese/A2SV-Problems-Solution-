class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        suf=[0]
        pre=[0]
        summ1=0
        summ2=0
        # j=len(customers)-1

        N_no=0
        all_yes=customers.count('Y')
        N_yes=0
        ans=all_yes
        j=0

        for i in range(len(customers)):
            if customers[i]=='Y':
                N_yes+=1
            elif customers[i]=="N":
                N_no+=1

            if ans>(all_yes-N_yes+N_no):
                j=i+1
                ans=all_yes-N_yes+N_no
            
            






        #     if customers[i]=='N':
        #         summ1+=1
        #     pre.append(summ1)

        #     if customers[j]=='Y':
        #         summ2+=1
        #     suf=[summ2]+suf
        #     j-=1
        # ans=float("inf")
        # j=0

        # for i in range(len(pre)):
        #     if ans>pre[i]+suf[i]:
        #         j=i
        #         ans=pre[i]+suf[i]
       
        return j
        



        