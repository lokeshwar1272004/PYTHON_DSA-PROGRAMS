nums = [2, -3, 2, 1]
"""i = 0
res = 0
maximum = 0
while i < len(nums):
    for j in range(i,len(nums)):
        maximum += nums[j]
        if maximum > res:
            res = maximum
    maximum = 0
    i += 1
print(res)"""

maximum = nums[0]
cursum = 0
for n in nums:
    if cursum < 0:
        cursum = 0
    cursum += n
    maximum = max(maximum, cursum)
print(maximum)
