class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
     
        pref=[]
        suf=[]
        j=len(s)-1

        summ=0
        summ1=0
        for i in range(len(s)):
            if int(s[i])==0:
                summ+=1
            pref.append(summ)

            summ1+=int(s[j])
            suf=[summ1]+suf
            j-=1
                    
        ans=0
     
        for i in range(len(s)-1):
            ans=max(ans,suf[i+1] +pref[i])
          
        
        
            
        return ans 


                    





