class Solution:
    def minOperations(self, boxes: str) -> List[int]:
      ans=[]
      location=[]
      for i in range(len(boxes)):
          if int(boxes[i])==1:
              location.append(i)
      for i in range(len(boxes)):
          acc=0
          for j in location:
              acc+=abs(j-i)
          ans.append(acc)
      return ans
        



        