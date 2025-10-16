n2 = list(map(int,input().split()))
n2=list(set(n2))
n2.remove(max(n2))
if n2:
    print(max(n2))
else:
    print(-2**3)

