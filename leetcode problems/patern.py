def rec(cur,n,p):
    new =p+str(cur)
    if cur == n:
        print(new)
        return
    print(new)
    rec(cur+1,n,new)
    print(new)
"rec(1,7,'')"

l = []
cur = 1
n= 5
while cur<n:
    if len(l)==0:
        print(str(cur))
        l.append(str(cur))

    else:
        p = l[-1] + str(cur)
        l.append(p)
        print(l[-1])
    cur+=1
i=len(l)-1
while i >= 0:
    print(l[i])
    i-=1




