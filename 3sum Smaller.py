def threeSum(nums, target):

    n = len(nums)
    nums = sorted(nums)
    summ = 0

    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            for k in range(j, n):
                if i == k or j == k:
                    continue
                elif nums[i]+nums[j]+nums[k] < target:
                    summ += 1
    return summ


def threesum(nums, target):
    n = len(nums)
    nums = sorted(nums)
    summ = 0
    for i in range(n):
        j = i+1
        k = n-1
        while j < k:
            if nums[i]+nums[j]+nums[k] < target:
                summ += k-j
                j += 1

            else:
                k -= 1
    return summ


def checker(L, target):
    if threeSum(L, target) == threesum(L, target):
        print(True)
    else:
        print(False)


checker([-2, 0, 1, -10, 10, 5, 3, 5, 8], 11)
