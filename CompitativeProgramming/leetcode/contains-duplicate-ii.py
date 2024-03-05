class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        tracker=defaultdict(list)

        for i in range(len(nums)):
            tracker[nums[i]].append(i)
        print(tracker)
        for key in tracker:
            if len(tracker[key])<2:
                continue 
            
            for i in range(len(tracker[key])-1):
                if abs(tracker[key][i]-tracker[key][i+1])<=k:
                    return True 
        return False
