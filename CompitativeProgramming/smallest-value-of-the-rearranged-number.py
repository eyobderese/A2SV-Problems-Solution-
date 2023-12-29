class Solution:
    def smallestNumber(self, num: int) -> int:
        num=str(num)
        num=(sorted(num))
        i=1
        if len(num)<2:
            return int(''.join(num))
            
        while num[0]=="0" :
            num[0],num[i]=num[i],num[0]
            i+=1
            if i==len(num):
                break
        if num[0]=='-':
            num=sorted(num[1:], reverse=True)
            num=['-']+num
            return int(''.join(num))

        
        return int(''.join(num))
        