class Solution:
    def plusOne(self, digits):
        if digits[-1]==9:
            s=""
            for i in digits:
                s=s+str(i)
            val=int(s)+1
            digits=[]
            for i in str(val):
                digits.append(int(i))
            return digits
        else:
            digits[-1]=digits[-1]+1
            return digits

            



        digits[-1]=digits[-1]+1
        