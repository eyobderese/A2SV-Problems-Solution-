class Solution:
    def isHappy(self, n: int) -> bool:

        tracker=[]
        val=0
        while True:
            for i in str(n):
                val+=int(i)**2
            if val==1:
                return True
            else:
                n=val
            
                if val in tracker:
                    return False
                tracker.append(val)
                val=0


                
        