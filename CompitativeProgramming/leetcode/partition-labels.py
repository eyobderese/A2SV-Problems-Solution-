class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # max_letter_apperance_dict={}
        # for index,letter in enumerate(s):
        #     max_letter_apperance_dict[letter]=index
        
        # start=0
        # end=0
        # answer=[]
        # for index,letter in enumerate(s):
        #     end=max(end,max_letter_apperance_dict[letter])

        #     if end==index:
        #         answer.append(end-start+1)
        #         start=end+1
        # return answer

        tracker={}
        for i in range (len(s)):
            tracker[s[i]]=i
        
        start=0
        end=0
        answer=[]

        for i in range(len(s)):
            end=max(end,tracker[s[i]])
            if i==end:
                answer.append(end-start+1)
                start=end+1
        return answer

        

        