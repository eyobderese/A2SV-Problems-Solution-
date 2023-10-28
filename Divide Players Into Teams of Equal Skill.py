from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        totalSkill = skill[0]+skill[-1]

        chemistry = 0

        while l < r:
            if skill[l]+skill[r] != totalSkill:
                return -1
            chemistry += (skill[l]*skill[r])
            l += 1
            r -= 1
        return chemistry
