class Solution:
    def frequencySort(self, s: str) -> str:
        comparator = {}
        for i in s:
            if i in comparator.keys():
                comparator[i] += 1
            else:
                comparator[i] = 1

        sortedDic = sorted(comparator.items(), key=lambda x: x[1])

        stringValue = ''
        for i in sortedDic:
            stringValue += (i[0]*i[1])

        return stringValue[::-1]
