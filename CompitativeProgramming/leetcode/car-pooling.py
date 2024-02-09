from operator import itemgetter

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    
        trips = sorted(trips, key=itemgetter(1))        

        currCup=0
        checker={}

        for cap,st,end in trips:
            currCup+=cap
    
            moreDict={}
            for key in checker: 
                if st>=key:
                    
                    currCup-=checker[key]
                else:
                    moreDict[key]=checker[key]
            checker=moreDict
            
            if currCup>capacity:
                return False
            
            if end in checker:
                checker[end]+=cap
            else:
                checker[end]=cap
        return True




        
       


            

        