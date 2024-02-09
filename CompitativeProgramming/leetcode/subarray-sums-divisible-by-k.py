class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

      

        
        dictTrack={i:0 for i in range(k)}
        dictTrack[0]+=1
        ans=0

        total=0
        for i in nums:              
            total+=i
            ans+=dictTrack[total%k]

            dictTrack[total%k]+=1
        return ans 