class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sortedPeople= sorted(people)
        bote=0
        i=0
        j=len(people)-1
        while i<=j:
            if sortedPeople[i] + sortedPeople[j] <= limit:
                bote+=1
                i+=1
                j-=1
            else:
                bote+=1
                j-=1
        return bote
        
                





       
                
