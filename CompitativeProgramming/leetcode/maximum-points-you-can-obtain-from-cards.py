class Solution:
    def maxScore(self, cardPoints, k):
        summ=sum(cardPoints)
        k=len(cardPoints)-k

        minn=float("inf")

        summ1=sum(cardPoints[:k])
        j=k
        i=0
        minn=min(summ1,minn)
        while j<len(cardPoints):
            summ1+=cardPoints[j]
            summ1-=cardPoints[i]
            i+=1
            j+=1
            minn=min(minn,summ1)
           
        return summ-minn


    

        

        