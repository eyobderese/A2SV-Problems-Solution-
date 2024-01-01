class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxRange=max(costs)+1
        box= [0]*maxRange
        for i in costs:
            box[i]+=1
        count=0
        for i in range(maxRange):
            while box[i]>0 and coins>=i:
                box[i]-=1
                count+=1
                coins-=i
            
            if coins<i:
                break
        return count


        