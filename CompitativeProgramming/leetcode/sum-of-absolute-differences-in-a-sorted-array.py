class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        summ1=0
        summ2=0

        pre=[]
        suf=[0]*len(nums)
        n=len(nums)
        j=len(nums)-1
        for i in range(len(nums)):
            summ1+=nums[i]
            pre.append(summ1)
            summ2+=nums[j]
            suf[j]=summ2
            j-=1
        print(pre,suf)

        ans=[]

        for i in range(len(nums)):
            numb=((i+1)*nums[i]) - pre[i]
            numb=numb+ (suf[i]-((n-i)*nums[i]))
            ans.append(numb)
        



        return ans
        