class Solution:
    def interpret(self, command: str) -> str:
     
        n=len(command)
        ans=''

        for i in range(n):
            if command[i]=='G':
                ans+='G'
            elif command[i]=="(":
               
                start=i
            elif command[start:i+1]=='()':
                ans+="o"
      
            elif command[start:i+1]=="(al)":
                ans+='al'
        return ans



        