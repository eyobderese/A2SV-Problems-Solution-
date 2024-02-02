class Solution:
    def minimumCardPickup(self, cards) :
        store=set()

        i=0
        j=0
        count=0
        ans=float('inf')

        while j<len(cards):
            flag=False
            
            while cards[j] in store:
                flag=True
                store.discard(cards[i])
                count-=1
                i+=1
                if i==len(cards):
                    flag=False
                    break
            if flag:
                ans=min(j-i+2,ans)
                if j>=len(cards):
                    break
            
            store.add(cards[j])
            count+=1
            j+=1
        return ans if ans!=float('inf') else -1


        