class Solution:
    def maxCoins(self, piles):
        result = 0
        sortedArray = sorted(piles)
        pointer = -2
        for i in range(len(piles)):
            if i < (len(piles)//3):
                result += sortedArray[pointer]
                pointer -= 2
        return result
