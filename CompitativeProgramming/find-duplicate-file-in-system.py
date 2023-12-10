class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        trackerdict={}

        for i in paths:
            files=i.split()
            for j in range(1,len(files)):
                indexOfPar=files[j].find('(')
                file=files[j][indexOfPar+1:len(files[j])-1]
                if file in trackerdict.keys():
                    trackerdict[file].append(files[0]+"/"+files[j][:indexOfPar])
                else:
                    trackerdict[file]=[files[0]+"/"+files[j][:indexOfPar]]
        ans=[]
        for key in trackerdict.keys():
            if len(trackerdict[key])>1:
                ans.append(trackerdict[key])
        return ans
                

        