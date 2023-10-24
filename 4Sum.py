def fourSum(nums, target):

    answer = []
    nums.sort()
    for i in range(len(nums)):
        for j in range(len(nums)):
            print('i = ', i)
            print('j = ', j)
            if i == j:
                continue
            k = j+1
            print('k = ', k)
            m = len(nums)-1
            print('m = ', m)

            print('****************************')

            while k < m:

                quadraplet = sorted([nums[i], nums[j], nums[k], nums[m]])
                summ = sum(quadraplet)
                if summ == target and quadraplet not in answer:
                    answer.append(quadraplet)
                    k += 1
                    m -= 1
                k += 1
                m -= 1

    return answer


print(fourSum([0, 0, 0], 0))
