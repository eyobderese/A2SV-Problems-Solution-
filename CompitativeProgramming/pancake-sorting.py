class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        k=len(arr)
        print(arr)
        while sorted(arr)!=arr:
            index=0
            i=0
            while i<k:
                
                if arr[i]>arr[index]:
                    index=i
                i+=1
            arr=arr[0:index+1][::-1] + arr[index+1:len(arr)] 
            ans.append(index+1)
            print(arr)

            arr=arr[:k][::-1]+arr[k:]
            print(arr)
            ans.append(k)
            k-=1
        return ans


#  [3,2,4,1]  2 3 
#  [4,2,3,1]  k
            
                

                
                          
        
            
     


        
        

            


        