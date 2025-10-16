nums=[4,5,6,7,0,1,2,3]
l = 0
r = len(nums)-1
target = 2

while l <= r:
    mid = (l+r)//2
    if nums[mid]==target:
        print(mid)
        break
    if nums[mid]>=nums[l]:
        if target >nums[mid] or nums[l]>target:
            l=mid+1
        else:
            r=mid-1
    else:
        if target < mid[nums] or nums[r]<target:
            r=mid-1
        else:
            l=mid+1



















