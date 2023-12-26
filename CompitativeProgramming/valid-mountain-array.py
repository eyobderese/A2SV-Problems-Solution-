class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr)<3:
            return False
        
       

        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
        
        k=0
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                k=i
                break
        arr1=arr[:i]
        arr2=arr[i:]
        if sorted(arr)==arr or sorted(arr,reverse=True)==arr:
            return False
        print(arr1,arr2)

        if arr1!=sorted(arr1) or arr2!=sorted(arr2, reverse=True):
            return False
        return True

        