a=9
n=[1,2,1,2,1,3,2]
d = {}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
paris=0
for j in d.keys():
    paris+=d[j]//2
print(paris)
print(d)