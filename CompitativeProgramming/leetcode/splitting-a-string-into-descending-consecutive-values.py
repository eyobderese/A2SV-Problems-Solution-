class Solution:
    def splitString(self, s: str) -> bool:

        def helper(index, prev):
            # print(index,len(s),prev)
            if index==len(s):
                return True
            
            for j in range(index,len(s)):
                val=int(s[index:j+1])
                if prev==val+1:
                    if helper(j+1,val):
                        return True
        for i in range(len(s)-1):
            val=int(s[:i+1])
            if helper(i+1,val):
                return True
        return False


                


            

       

                
                


        