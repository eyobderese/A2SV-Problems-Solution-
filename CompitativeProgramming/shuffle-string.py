class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tracker_dict={}
        for i in range(len(s)):
            tracker_dict[indices[i]]=s[i]
        answer=""
        for i in range(len(s)):
            answer+=tracker_dict[i]
        return answer


            
