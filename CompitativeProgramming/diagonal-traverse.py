class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        tracker=defaultdict(list)
        n=len(mat)
        m=len(mat[0])

        j=0
        while j<n:
            i=0
            while i<m:
                tracker[i+j].append(mat[j][i])
                i+=1
            j+=1
        ans=[]
        flag=True
        for i in tracker.keys():
            if flag:
                ans+=(tracker[i][::-1])
                flag=False
            else:
                ans+=(tracker[i])
                flag=True
        return ans

           
