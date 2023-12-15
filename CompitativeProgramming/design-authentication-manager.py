class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.tracker={}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tracker[tokenId]=currentTime+self.timeToLive
        
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tracker:
            if self.tracker[tokenId]>currentTime:
                self.tracker[tokenId]=self.timeToLive+currentTime
            

        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for i in self.tracker.values():
            if i>currentTime:
                count+=1
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)