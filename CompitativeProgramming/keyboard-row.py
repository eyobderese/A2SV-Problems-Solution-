class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        ans=[]

        for word in words:
            
            firstletter=word[0]
            if firstletter.lower() in row1:
                flag=True
                for letter in word:
                    if letter.lower() not in row1:
                        flag=False
                        break
                if flag:
                    ans.append(word)
            if firstletter.lower() in row2:
                flag=True
                for letter in word:
                    if letter.lower() not in row2:
                        flag=False
                        break
                if flag:
                    ans.append(word)
            if firstletter.lower() in row3:
                flag=True
                for letter in word:
                    if letter.lower() not in row3:
                        flag=False
                        break
                if flag:
                    ans.append(word)
        return ans
                
            


        