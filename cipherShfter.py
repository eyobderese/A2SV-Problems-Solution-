
def sypherShiphter(s):
    isadded = False
    target = s[0]
    aanswer = ''
    i = 1
    while i < len(s)-2:
        if target == s[i]:
            isadded = not isadded
            target = s[i+1]
            print("target: ", target)
        if not isadded:
            i += 1
        else:
            aanswer += s[i]
            isadded = not isadded
            i += 1
    print(aanswer)


s = "abacabac"

sypherShiphter(s)
