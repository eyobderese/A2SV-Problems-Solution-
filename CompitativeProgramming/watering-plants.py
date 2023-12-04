class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count=0
        realCapacity=capacity
        for i in range(len(plants)):
            print(count)
            if plants[i]>capacity:
                count+=2*(i)+1
                capacity=realCapacity-plants[i]
            else:
                count+=1
                capacity-=plants[i]     
        return count



        