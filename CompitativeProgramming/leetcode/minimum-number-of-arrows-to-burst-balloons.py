class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points=sorted(points)

        i=len(points)-2

        count=1
        brustPoint=points[-1][0]
        print(points)
        while i>=0:
            if points[i][1]>=brustPoint and brustPoint>=points[i][0] :
                i-=1
                continue
            else:
                count+=1
                brustPoint=points[i][0]
                i-=1
            
        return count
        


           


        j-=1
        return count





        