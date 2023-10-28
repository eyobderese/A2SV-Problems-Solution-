class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c**(1/2))
        while i <= j:
            if i**2 + j**2 == c:
                return True
            elif i**2 + j**2 > c:
                j -= 1
            else:
                i += 1

        return False
