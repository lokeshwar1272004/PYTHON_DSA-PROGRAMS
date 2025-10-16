n ='"AAABABB'
k=2
d={}
for i in range(len(n)):
    if i not in d:
        d[i]=1
    else:
        d[i]+=1