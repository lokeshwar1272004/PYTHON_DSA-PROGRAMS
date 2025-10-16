"""5 4
1 2 3 4 5"""

a,b=map(int,input().split())
arr=list(map(int,input().split()))
print(arr)

for i in range(b):
    x=arr.pop(0)
    arr.append(x)
print(arr)
s=''
for j in arr:
    s+=str(j)+' '
print(s)