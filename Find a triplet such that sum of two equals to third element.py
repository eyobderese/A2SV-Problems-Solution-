def Findtriplet(arry):
    i = len(arry)-1
    while i > 2:
        k = 0
        j = i-1
        arry.sort()

        while k < j:
            left = arry[k]
            right = arry[j]
            target = arry[i]
            if left+right == target:
                print(left, right, target)

                return
            elif left+right > target:
                j -= 1

            else:
                k += 1

        i -= 1
    print('sorry no such tapilet')


Findtriplet([5, 32, 1, 7, 10, 50, 19, 21, 0])
