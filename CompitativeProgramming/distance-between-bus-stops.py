class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination<start:
            start,destination=destination,start
        n=len(distance)
        summ=sum(distance[start:destination])
     
        summ1=sum(distance[destination-n:])+ sum(distance[0:start])
        return min(summ,summ1)
        