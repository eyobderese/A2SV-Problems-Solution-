

def doNotDest(s):
    tracker=[s[0]]
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            continue
        elif s[i+1] not in tracker:
            
            tracker.append(s[i])
        else:
            print('NO')
            return 0
    print('Yes')
  



x=int(input())
while x>0:
    unnessecery=input()

    s=input()
    doNotDest(s)

    x-=1



