class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k=0
        for i in range(len(arr2)):
            m=arr2[i]


            
            j=k
            while j<len(arr1):
                if arr1[j]==m:
                    arr1[k],arr1[j]=arr1[j],arr1[k]
                    print(arr1[k],arr1[j])
                    k+=1
                j+=1
        arr1=arr1[:k]+sorted(arr1[k:])
        return arr1
            


  


        