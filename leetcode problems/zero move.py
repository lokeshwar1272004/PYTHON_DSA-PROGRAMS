nums = [0,1,0,3,2]
l=len(nums)-1
i=0
j=0
while j<l:
    j+=1
    if nums[i]!=0:
        i+=1
    if nums[j]!=0:
        nums[j],nums[i]=nums[i],nums[j]

print(nums)
nums_2 = [0,1,0,3,2]
i=len(nums_2)-1
j = len(nums_2)-1
while j>0:
    j-=1
    if nums_2[i]!=0:
        i-=1
    if nums_2[j]!=0:
        nums_2[j], nums_2[i] = nums_2[i], nums_2[j]

print(nums_2)
