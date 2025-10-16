nums=[-2,1,-3,4,-1,2,1,-5,4]

maximum=nums[0]
cur_sum=0
for i in range(len(nums)):
    if cur_sum<0:
        cur_sum=0
    cur_sum+=nums[i]
    maximum=max(maximum,cur_sum)
print(maximum)

haystack ="sadbutsad"
needle ="ts"

for i in range(len(haystack)+1-len(needle)):
    if haystack[i:i+len(needle)]==needle:
        print(i)
        break
