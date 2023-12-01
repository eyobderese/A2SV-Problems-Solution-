class Solution:
    def romanToInt(self, s: str):
        val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        summ=0
        
        i=0
        while len(s)>1:
            flag=False
            if s[0]=="I" and s[1]=="V":
                s=s[2:]
                summ+=4
            elif s[0]=="I" and s[1]=="X":
                summ+=9
                s=s[2:]
                flag=True
            elif s[0]=="X" and s[1]=="L":
                summ+=40
                s=s[2:]
                flag=True
            elif s[0]=="X" and s[1]=="C":
                summ+=90
                s=s[2:]
                flag=True
            elif s[0]=="C" and s[1]=="D":
                summ+=400
                s=s[2:]
                flag=True
            elif s[0]=="C" and s[1]=="M":
                summ+=900
                s=s[2:]
                flag=True
            else:
                summ+=val[s[i]]
                s=s[1:]
        if len(s)!=0:
            summ+=val[s]

        return summ

