def maximum(nums):
    maxsub=nums[0]
    cursum=0

    for n in nums:
        if cursum<0:
            cursum=0
        cursum+=n
        maxsub=max(maxsub,cursum)
    return maxsub
nums=[2,3,4,-1,-2,1]
#nums=[-1,-2,-1]
print(maximum(nums))

alpha=[3,4,2,1,3]
target=7
d={}
for i in range(len(alpha)):
    difference=target-alpha[i]
    if alpha[i] not in d:
        d[difference]=i
    else:
        print(i,d[alpha[i]])
        break





a=[-1,-2,-3,-4]
m=a[0]
c=0
for i in a:
    if i <0:
        c=0
    c+=i
    m=max(m,c)
print(m)
