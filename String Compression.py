from ast import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)

        j = 0
        s = ''

        while j < n:
            counter = 1
            while j < n-1:
                if chars[j] == chars[j+1]:
                    counter += 1
                    j += 1
                else:
                    break

            if counter > 1:
                s += chars[j]
                s += str(counter)
                j += 1
            else:
                s += chars[j]
                j += 1
        for index, element in enumerate(list(s)):
            chars[index] = element
        return len(s)
