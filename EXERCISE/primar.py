def perim(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a = 20
num =2
ans = []
while num < a:
    if perim(num):
        ans.append(num)
    num+=1
print(ans)
