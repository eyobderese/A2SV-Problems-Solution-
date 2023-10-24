import heapq


def largest(nums, k):
    nums.sort()
    i = 0
    j = len(nums)-1

    while j > i:
        if nums[i]+nums[j] == k:
            return nums[i], nums[j]
        elif nums[i]+nums[j] > k:
            j -= 1
        else:
            i += 1


# print(largest([3, 2, 1, 5, 6, 4], 8))


def gatherZero(nums):
    s = 0
    p = 0

    while p < len(nums):
        if nums[s] != 0:
            s += 1
            p += 1
        else:
            while nums[p] == 0:
                p += 1
            nums[p], nums[s] = nums[s], nums[p]
            p = s

    return nums

# print(gatherZero([1, 2, 5, 0, 5, 0, 9]))


def validPalindrome(s):
    i = 0
    j = len(s)-1
    isDeleted = True

    while i <= j:
        print('i is ', i, 'j is ', j)
        if s[i] == s[j]:
            i += 1
            j -= 1
        elif isDeleted:
            s = s.replace(s[j], '')
            isDeleted = False
            j -= 1

        else:
            return False
    return True


# print(validPalindrome('eedede'))
nums = [5207, 5594, 477, 6938, 8010, 7606, 2356, 6349, 3970, 751, 5997, 6114, 9903, 3859, 6900, 7722, 2378, 1996, 8902, 228, 4461, 90, 7321, 7893, 4879, 9987, 1146, 8177, 1073, 7254, 5088, 402, 4266, 6443, 3084, 1403, 5357, 2565, 3470, 3639, 9468, 8932, 3119, 5839, 8008, 2712, 2735, 825, 4236, 3703, 2711, 530, 9630, 1521, 2174, 5027, 4833, 3483, 445, 8300, 3194,
        8784, 279, 3097, 1491, 9864, 4992, 6164, 2043, 5364, 9192, 9649, 9944, 7230, 7224, 585, 3722, 5628, 4833, 8379, 3967, 5649, 2554, 5828, 4331, 3547, 7847, 5433, 3394, 4968, 9983, 3540, 9224, 6216, 9665, 8070, 31, 3555, 4198, 2626, 9553, 9724, 4503, 1951, 9980, 3975, 6025, 8928, 2952, 911, 3674, 6620, 3745, 6548, 4985, 5206, 5777, 1908, 6029, 2322, 2626, 2188, 5639]
print(sum(nums))
