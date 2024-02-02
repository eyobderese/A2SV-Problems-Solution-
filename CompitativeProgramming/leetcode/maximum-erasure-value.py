class Solution:
    def maximumUniqueSubarray(self, nums):
        store=set()
        j=0
        i=0
        ans=0
        summ=0
        flag=True

        while j<len(nums):

            while nums[j] in store:

                summ-=nums[i]
                store.discard(nums[i])
                i+=1
                if i==len(nums):
                    flag=False
                    break
            if flag:
                store.add(nums[j])
                summ+=nums[j]
            ans=max(ans,summ)
            j+=1
        return ans



