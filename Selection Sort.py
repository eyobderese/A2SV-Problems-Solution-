class Solution:
    def select(self, arr, i):
        # code here
        index = i
        for j in range(i, len(arr)):

            if arr[j] < arr[index]:
                index = j

        return index

    def selectionSort(self, arr, n):
        # code here
        i = 0
        while i < len(arr):
            index = self.select(arr, i)

            arr[index], arr[i] = arr[i], arr[index]
            i += 1
        return arr
