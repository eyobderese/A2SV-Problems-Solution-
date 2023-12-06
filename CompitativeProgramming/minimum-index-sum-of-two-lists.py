class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        minIndex=float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    sumIndex=i+j
                    if minIndex>sumIndex:
                        ans=[list1[i]]
                        minIndex=sumIndex
                    elif minIndex==sumIndex:
                        ans.append(list1[i])
        return ans 


        