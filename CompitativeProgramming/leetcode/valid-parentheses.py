class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        dic={"{": '}',"[":"]","(":")"}
        for i in s:
            if i in dic.keys():
                stack+=[i]
            else:
                if len(stack)!=0:
                    m=stack.pop()
                    if dic[m]!=i:
                        return False
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
        

        
