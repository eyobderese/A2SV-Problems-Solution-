class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)

        i=0
        ans=[]
        while i<n:
            j=n-1
            row=[]
            while j>=0:
                if image[i][j]==1:
                    row.append(0)
                    j-=1
                else:
                    row.append(1)
                    j-=1
            ans.append(row)
            i+=1
        return ans

    

        
            

        