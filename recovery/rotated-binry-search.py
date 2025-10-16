"""nums = [3,4,5,6,1,2]
nums = [4,5,0,1,2,3]
Input: nums = [4,5,6,7]
target small element-0(log n) """
#nums=[3,4,5,6,1,2]
nums = [4,5,0,1,2,3]
l=0
r=len(nums)-1
while l < r:
    mid=(l+r)//2
    if nums[l]>nums[r] and nums[mid]>nums[r]:
        l=mid+1
    elif nums[l]>nums[r] and nums[mid]<nums[r]:
        r=mid
    elif nums[l]<=nums[r]:
        return l
return l