class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime= sorted(processorTime)[::-1]
        tasks=sorted(tasks)
    
        maxx=0
        j=0

        for i in processorTime:
            k=0
            while k<4:
                maxx=max(maxx,tasks[j+k]+i)
                k+=1            
            j+=4
        return maxx



        