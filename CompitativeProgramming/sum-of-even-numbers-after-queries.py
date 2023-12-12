class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum=sum(filter(lambda x:x%2==0,nums))
        ans=[]

        for i,j in queries:
            if nums[j]%2==0:
                x=nums[j]
                nums[j]+=i
                if i%2==0:
                    evenSum+=i
                    ans.append(evenSum)
                else:
                    evenSum-=x
                    ans.append(evenSum)


            else:
                x=nums[j]
                nums[j]+=i
                if i%2==0:
                    ans.append(evenSum)

                else:
                    evenSum+=nums[j]
                    ans.append(evenSum)
        return ans


            


            

        
            


        