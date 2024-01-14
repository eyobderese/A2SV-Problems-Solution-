class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        firstList=[]
        secondList=[]

        i=0
        j=0
        while i<len(name):
            while name[i]==name[j]:
                j+=1
                if j>=len(name):
                    break

            firstList.append([name[i],j-i])
            i=j
           

        i=0
        j=0
        while i<len(typed):
            while typed[i]==typed[j]:
                j+=1
                if j>=len(typed):
                    break

            secondList.append([typed[i],j-i])
            i=j
        
        if len(firstList)!=len(secondList):
            return False
        
        for i in range(len(firstList)):
            if firstList[i][0]==secondList[i][0] and firstList[i][1]<=secondList[i][1]:
                continue
            else:
                return False
        return True
        


        

       

            
        
    



        