class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N=len(deck)
        deck.sort()

        ans=[None]*N
        i=0
        while deck:
            ans[i]=deck.pop(0)
            temp=self.findNextEmpity(ans,i+1)
            i=self.findNextEmpity(ans,temp+1)
        return ans

    def findNextEmpity(self,out,index):
        while index<len(out):
            if out[index]==None:
                return index
            index+=1
        i=0
        while i<len(out) and i<index:
            if out[i]==None:
                return i
            i+=1

        return i


        
        
    
        


        