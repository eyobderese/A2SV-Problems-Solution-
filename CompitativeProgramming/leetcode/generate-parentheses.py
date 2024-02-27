class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        store = []
        tracker=set()

        def helper(temp):
            nonlocal store
            if len(temp)==2*n:
                ans=''.join(temp)
                if self.validate(temp) and ans not in tracker:
                    
                    store.append(ans)
                    tracker.add(ans)
                return
            
            for par in ["(",")"]:
                temp.append(par)
                helper(temp)
                temp.pop()

        helper([])
        return store 

    def validate(self,s):
        open_count = 0
        for char in s:
            if char == "(":
                open_count += 1
            elif char == ")":
                if open_count == 0:
                    return False
                open_count -= 1
        return open_count == 0
       



        




        