class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """

        answers.sort()

        count=0
        tracker=0
        currVal=None
        i=0

        for i in range(len(answers)):
            if tracker==0 or currVal!=answers[i]:
                count+=(answers[i]+1)
                tracker=answers[i]
                currVal=answers[i]
            elif currVal==answers[i]:
                tracker-=1
            i+=1
        return count
            


            

            
