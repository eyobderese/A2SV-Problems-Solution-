class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store={}
        store[2]=["a","b","c"]
        store[3]=["d","e","f"]
        store[4]=["g","h","i"]
        store[5]=["j","k","l"]
        store[6]=["m","n","o"]
        store[7]=["p","q","r","s"]
        store[8]=["t","u","v"]
        store[9]=["w","x","y","z"]
        out=[]
        n=len(digits)
        digits=list(map(int,list(digits)))        
        allDigit=[]
        for i in digits:
            allDigit.append(store[i])
        for ans in itertools.product(*allDigit):
            out.append(''.join(ans))

        return out if out[0] else []


                

            


            

            

        