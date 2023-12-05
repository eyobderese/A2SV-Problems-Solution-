class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]

        mydict={str(i):i for i in range(10)}

        number1=0
        number2=0
        multiplay=1

        for i in num1:
            number1+=mydict[i]*multiplay
            multiplay*=10
        multiplay=1
        for i in num2:
            number2+=mydict[i]*multiplay
            multiplay*=10
        return str(number1*number2)
        
        


        
        
        
        
       
       
       
       
       
        # return str(int(num1)*int(num2))