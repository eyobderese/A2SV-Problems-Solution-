def maxArea(height):
    l=0
    r=len(height)-1

    maxWater=0

    while r>l:
        

        if height[l]<height[r]:
            maxWater=max(maxWater,height[l]* (r-l))
            l+=1
        else:
            maxWater=max(maxWater,height[r]* (r-l))
            r-=1
    return maxWater


