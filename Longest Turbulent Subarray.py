from collections import defaultdict


def maxTurbulenceSize(arr):
    counter = 1
    ans = 0
    isgrater = True
    isleas = True
    i = 0
    j = 1

    while j < len(arr):
        print("counter is: ", counter)
        if arr[i] > arr[j] and isleas:
            j += 1
            i += 1
            isleas = False
            isgrater = True
            counter += 1
        elif arr[i] < arr[j] and isgrater:
            j += 1
            i += 1
            isleas = True
            isgrater = False
            counter += 1
        elif arr[i] == arr[j]:
            i = j
            j += 1
            ans = max(ans, counter)
            counter = 1
        else:
            ans = max(ans, counter)
            isgrater = True
            isleas = True
            j = i
            j += 1
            counter = 1
    return ans


print(maxTurbulenceSize([0, 8, 45, 88, 48, 68, 28, 55, 17, 24]))
