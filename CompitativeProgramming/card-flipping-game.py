class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
       
        naverAnswer=set()
       
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                naverAnswer.add(fronts[i])
        combind=fronts+backs
        combind.sort()
        for i in combind:
            if i not in naverAnswer:
                return i
        return 0

         
       
        
        
 

        

        