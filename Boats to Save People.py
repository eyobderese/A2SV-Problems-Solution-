from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sortedPeople = sorted(people)
        boat = 0
        i = 0
        j = len(people)-1
        while i <= j:
            if sortedPeople[i] + sortedPeople[j] <= limit:
                boat += 1
                i += 1
                j -= 1
            else:
                boat += 1
                j -= 1
        return boat
