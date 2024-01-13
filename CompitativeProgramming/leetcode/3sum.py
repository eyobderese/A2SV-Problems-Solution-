class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+ nums[l] + nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    triplet =[nums[i],nums[l],nums[r]]
                    if triplet not in answer:
                        answer.append(triplet)
                    while l<r and nums[l] == triplet[1]:
                        l+=1
                    while l<r and nums[r]==triplet[2]:
                        r-=1
        return answer

            



        

                