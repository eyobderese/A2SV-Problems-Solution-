class Solution:
    def maxConsecutiveAnswers(self, answerKey,k):
        count=0

        i=0
        j=0
        ans=[]

        while j<len(answerKey):
            if answerKey[j]=="F":
                count+=1
            if count>k:
                ans.append(j-i)
                while answerKey[i]=="T":
                    i+=1
                i+=1
                count-=1
            j+=1
            # print(i,j)
        if count<=k:
            ans.append(j-i)

        forTrue=max(ans)
        i=0
        j=0
        ans=[]
        count=0

        while j<len(answerKey):
            if answerKey[j]=="T":
                count+=1
            if count>k:
                ans.append(j-i)
                while answerKey[i]=="F":
                    i+=1
                i+=1
                count-=1
            j+=1
            # print(i,j)
        if count<=k:
            ans.append(j-i)

        forFalse=max(ans)

        return(max(forTrue,forFalse))


        

        




        