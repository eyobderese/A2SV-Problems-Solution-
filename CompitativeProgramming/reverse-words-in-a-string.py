class Solution:
    def reverseWords(self, s: str) -> str:
        m=(s.split())[::-1]
        return ' '.join(m)

        