def calculate(s):
    s=s.strip()
    if s.isdigit():
        return int(s)

    s='(' + s + ')'
    stack=[]
    for i in s:
        if i!=")" :
            if i==" ":
                continue
            elif i!='+' and i!='-' and i!='(':
                stack.append(int(i))

            else:
                stack.append(i)  [(1+(4+5+2)-3+(6+8))]
        else:
            value=0
            m=0
            n=0
            while n!='(':
                m=stack.pop()
                n=stack.pop()

                if n=='-':
                    value-=m
                elif n=='+' or n=='(':
                    value+=m
            stack.append(value)
    return stack[0]

