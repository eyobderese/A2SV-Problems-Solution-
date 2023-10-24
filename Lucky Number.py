# # t = list(map(int, input().split()))


# def lackiest(l, m):
#     lacky = float('-inf')
#     s = ''

#     for i in range(l, m+1):

#         zeros = i % 10
#         ones = i//10

#         if ones > 9:
#             ones = ones//101

#         if lacky <= abs(zeros-ones):
#             s = ''
#             lacky = abs(zeros-ones)
#             s = s+str(ones)+str(zeros)

#     print(int(s))


# testcase = int(input())


# def solve():
#     l, r = map(int, input().split())
#     cnt = l
#     ans = float('-inf')
#     for i in range(l, r+1):
#         s = str(i)
#         maxi = -1
#         mini = 10
#         for j in range(len(s)):
#             maxi = max(maxi, int(s[j]))
#             mini = min(mini, int(s[j]))
#         if maxi - mini == 9:
#             print(i)
#             return
#         if maxi - mini > ans:
#             ans = maxi - mini
#             cnt = i
#     print(cnt)


# def main():
#     t = int(input())
#     for _ in range(t):
#         solve()


# if __name__ == "__main__":
#     main()


def lackines(l, m):
    ans = l
    maxLack = 0
    for i in range(l, m+1):
        stri_numb = ''.join(sorted(str(i)))
        diff = int(stri_numb[-1])-int(stri_numb[0])
        if diff > maxLack:
            ans = i
            maxLack = diff
        if maxLack == 9:
            break
    print(ans)


testcase = int(input())
for _ in range(testcase):
    l, r = map(int, input().split())
    lackines(l, r)
