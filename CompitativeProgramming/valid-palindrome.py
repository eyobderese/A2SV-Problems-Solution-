class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        s = ''.join(letter for letter in s if letter.isalnum())
        for i in range(1,len(s)):
            if s[i-1]!=s[-i]:
                return False
        return (True)
        