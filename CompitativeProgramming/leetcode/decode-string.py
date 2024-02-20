class Solution:
    def decodeString(self, s: str) -> str:
        digitStack=[]
        charStack=[]
        i=0
        while i < (len(s)):
            if s[i].isdigit():
                n=''
                while s[i].isdigit():
                    n+=s[i]
                    i+=1
                digitStack.append(int(n))
                continue
            elif s[i]=="]":
                m=""
                while charStack and charStack[-1]!="[":
                    n=charStack.pop()
                    m=n+m
                n=digitStack.pop()
                charStack.pop()
                charStack.append(m*n)
            else:
                charStack.append(s[i])
            i+=1
        return "".join(charStack)






        



    

    def decodeHelper(self,s):
        if len(s)==0:
            return ""
        if len(s)==1:
            return int(s[0][0])*s[0][2:] if len(s[0])>1 else ""
        multiplayer=int(s[0][0])
        return (multiplayer*s[0][2:])+ self.decodeHelper(s[1:])

        