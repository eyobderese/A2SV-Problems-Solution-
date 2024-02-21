class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        arr=list(senate)
        que= deque(arr)
        countOnD=0
        countOnR=0

        while True:
            if que[0]=="D":
                N=len(que)
                i=0
                while que[0]=='D':
                   
                    if countOnD:
                        que.popleft()
                        countOnD-=1
                    elif not countOnD:
                        countOnR+=1
                        D=que.popleft()
                        que.append(D)
                    
                    i+=1
                    if i==N:
                        return "Dire"
              
            elif que[0]=="R":
                N=len(que)
                i=0
                while que[0]=='R':
                    if countOnR:
                        que.popleft()
                        countOnR-=1
                    elif not countOnR:
                        countOnD+=1
                        R=que.popleft()
                        que.append(R)
                        i+=1
                    if i==N:
                        return "Radiant"
              
                        
        

        