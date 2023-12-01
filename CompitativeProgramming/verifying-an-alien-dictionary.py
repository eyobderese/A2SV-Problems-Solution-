class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for i in range (len(words)-1):
            x=order.find(words[i][0])
            y=order.find(words[i+1][0])

            if x>y:
                return False
            elif x==y:
                j=i
                flag=True
                while x==y and len(words[i])>j and len(words[i+1])>j:
                    x=order.find(words[i][j])
                    y=order.find(words[i+1][j])
                    if x>y:
                        return False
                    if x<y:
                        flag=False
                        break
                    else:
                        j+=1
                if flag and len(words[i])>len(words[i+1]):
                    return False
        return True

        

                    



            
            
        