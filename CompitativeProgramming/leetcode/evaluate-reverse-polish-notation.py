class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in tokens:
            
            if i == '+':
                n = stack.pop()
                m = stack.pop()
                res = m+n
                stack.append(res)
            elif i == '-':
                n = stack.pop()
                m = stack.pop()
                res = m-n
                stack.append(res)
            elif i == '/':
                n = stack.pop()
                m = stack.pop()
                res = int(m/n)
                stack.append(res)
            elif i == '*':
                n = stack.pop()
                m = stack.pop()
                res = m*n
                stack.append(res)
            else:
                stack.append(int(i))
        return int(stack[0])