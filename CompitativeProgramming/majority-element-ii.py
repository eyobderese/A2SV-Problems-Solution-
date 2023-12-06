
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counterDic=Counter(nums)
        answer=[]
        for i in counterDic:
            if counterDic[i]>len(nums)//3:
                answer.append(i)
        return answer




        