class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums1:
            print(i)
            x=nums2.index(i)
            flag=True
            for j in nums2[x:]:
                if j>i:
                    ans.append(j)
                    flag=False
                    break
            if flag:        
                ans.append(-1)
        return ans
        