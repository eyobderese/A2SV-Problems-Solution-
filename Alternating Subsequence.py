

# def subSequence(arry):
#     maxx = float('-inf')
#     i = 0
#     j = 1
#     k = 0
#     maxLength = 0
#     dictMaxTracker = {}

#     while j < len(arry):

#         maxLength = max(maxLength, j-i)

#         if maxLength in dictMaxTracker:

#             maxx = max(dictMaxTracker[maxLength], sum(arry[i:j]))
#             dictMaxTracker[maxLength] = maxx
#         else:

#             dictMaxTracker[maxLength] = sum(arry[i:j])

#         if (arry[k] > 0 and arry[j] > 0) or (arry[k] < 0 and arry[j] < 0):
#             i = j
#             j += 1
#             k += 1

#         elif (arry[k] > 0 and arry[j] < 0) or (arry[k] < 0 and arry[j] > 0):
#             k += 1
#             j += 1
#     print(dictMaxTracker)
#     return dictMaxTracker[max(dictMaxTracker)]


# print(subSequence([-2, 8, 3, 8, -4, -15, 5, -2, -3, 1]))


# # testCase = int(input())

# # while testCase > 0:
# #     arrayLength = input()
# #     firstArray = list(map(int, input().split()))
# #     print(subSequence(firstArray))


# #     testCase -= 1
