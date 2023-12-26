class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            j=0
            isSorted=True
            while j<len(heights)-1:
                
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    names[j],names[j+1]=names[j+1],names[j]
                    j+=1
                    isSorted=False
                else:
                    j+=1
            if isSorted:
                return names[::-1]
        return names[::-1]

                    



        