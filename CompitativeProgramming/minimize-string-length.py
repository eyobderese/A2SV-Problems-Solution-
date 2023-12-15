class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s=list(s)
        counter= Counter(s)
        return len(counter)
        # return len(set(list(s)))
        