def target(nums,t):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == t:
            return mid
        if t > nums[mid]:
            l=mid+1
        else:
            r=mid-1
    return l

n = [1,3,5,6]
print(target(n,t=5))