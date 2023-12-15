class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        tracker=defaultdict(int)
        for i in cpdomains:
            listSub=i.split()
            val=int(listSub[0])
            
            domain='.'+listSub[1]
            for i in range(1,len(domain)+1):
                if domain[-i]==".":
                    tracker[domain[len(domain)-(i-1):]]+=val
        ans=[]
        for i in tracker.keys():
            ans.append(str(tracker[i])+" "+ i)
        return ans



        
