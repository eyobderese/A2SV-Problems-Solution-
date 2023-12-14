class UndergroundSystem:

    def __init__(self):
        self.dec={}
        self.str={}
        self.strend=defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dec[id]=t
        self.str[id]=stationName
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stName=self.str[id] +'/'+ stationName
        self.strend[stName].append(t-self.dec[id])


        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stName=startStation+'/'+endStation
        return sum(self.strend[stName])/len(self.strend[stName])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)