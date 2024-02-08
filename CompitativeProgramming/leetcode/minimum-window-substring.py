class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        store= defaultdict(int)
        ans=float("inf")
        ans_string=""
        need=0
        for i in t:
            store[i]+=1
            need+=1
        

        
        left=0
        tracker=defaultdict(int)
        have=0
        i=0
        j=len(s)
        flag=False
        for right in range(len(s)):
            if s[right] in store:
                
                tracker[s[right]]+=1
                if store[s[right]]>=tracker[s[right]]:
                    have+=1
            
            

            while have>=need:
                flag=True
                if j-i>right-left:
                    i,j=left,right+1

                if s[left] in store:
                    
                    if tracker[s[left]]<=store[s[left]]:
                        have-=1
                    tracker[s[left]]-=1
                left+=1
            
            
               
                    
                    

              
        return s[i:j] if flag else ""
            

            
        
        

        