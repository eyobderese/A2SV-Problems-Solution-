class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        windoSize = len(s1)

        s1 = ''.join(sorted(s1))

        for i in range(len(s2)-len(s1)+1):
            temp = ''.join(sorted((s2[i:i+windoSize])))

            if s1 == temp:
                return True
        return False
