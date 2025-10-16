a=[1,2,3,4,0]
b=[3,2,5,6,6]
i=j=0
n=len(i)<
while i<len(a) and j<len(b):
    if a[i]<=b[j]:
        a[i]=a[i]
        i+=1
    else:
        a[i]=b[j]
        j+=1
print(a)