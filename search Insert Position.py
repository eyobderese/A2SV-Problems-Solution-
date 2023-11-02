def searchInsert(nums,target):
    low=0
    high=len(nums)
    while low<high:
        print('low: ',low, "high: ",high )
        mid=(low+high)//2
        
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        else: low=mid+1
    return mid+1

print(searchInsert([1,3,5,6],2))