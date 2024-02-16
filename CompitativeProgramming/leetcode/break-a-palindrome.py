class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        
        s=list(palindrome)
        if len(palindrome)==1:
            return ""
        # counter=Counter(s)
        # if len(counter)==1 and s[0]=="a":
        #     s[-1]="b"
        #     return str(s)

        else:
            for i in range(len(s)):
                if s[i]!="a":
                    if len(s)%2!=0 and i==len(s)//2:
                        continue
                    s[i]="a"
                    return "".join(s)
            s[-1]="b"
            return ''.join(s)

