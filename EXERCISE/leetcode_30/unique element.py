#nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]

l = 1
for r in range(1,len(nums)):
    if nums[r-1]!=nums[r]:
        nums[l]=nums[r]
        l+=1
print(l)

val=1
# nums = [3,2,2,3],
nums = [3,2,2,3,1]
l=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[l]=nums[i]
        l+=1
print(l)