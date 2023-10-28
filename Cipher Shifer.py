def Cipher_Shifer(s):
    i = 0
    j = 0
    ans = ''

    while j < len(s):

        if s[j] != s[i]:
            j += 1

        elif j == i:
            ans += s[i]
            j += 1

        else:
            j += 1
            i = j
    print(ans)


x = int(input())

for i in range(x):
    m = input()
    Cipher_Shifer(input())
