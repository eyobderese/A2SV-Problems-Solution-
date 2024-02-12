class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        store=defaultdict(list)
        ans=[0]*len(nums)

        for i in range(len(nums)):
            store[nums[i]].append(i)
        for key in store:
            arry=store[key]
            summ=0
           
            j=len(store[key])-1
            pre=[0]
            
            for i in arry:
                summ+=i
                pre.append(summ)
                
            for pointer,val in enumerate(arry):
                answer=pre[-1]-pre[pointer]-((len(pre)-pointer)*val) +(((pointer+1)*val)-pre[pointer])
                ans[val]=answer
                

        return ans



        
                

        


        