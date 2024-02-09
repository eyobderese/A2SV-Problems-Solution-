class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        arr=list(s)
        i=0
        j=len(arr)-1
        count=0
        while i<j:
            while arr[i]!="1":
                i+=1
                if i>=len(arr):
                    break
            while arr[j]!="0":
                j-=1
                if j<0:
                    break
            if i>j:
                break
            count+=(j-i)
            arr[j],arr[i]=arr[i],arr[j]
        return count

            

                    
            
            
        return count
        