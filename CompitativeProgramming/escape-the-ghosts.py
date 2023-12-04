class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        minn=float('inf')
        for x,y in ghosts:
            minn=min(minn,abs(x-target[0])+abs(y-target[1]))
        if abs(target[0])+abs(target[1])<minn:
            return True
        return False


        