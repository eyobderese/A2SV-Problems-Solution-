from ast import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        counter = 1
        ans = 1
        isgrater = True
        isleas = True
        i = 0
        j = 1

        while j < len(arr):

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
        ans = max(ans, counter)

        return ans
