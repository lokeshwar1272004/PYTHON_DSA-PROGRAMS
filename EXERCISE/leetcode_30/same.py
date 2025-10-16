a=[1,2,2,1,1,3]

d= {}
for i in a:
    if i not in d:
        d[i]=0
    d[i]+=1
print(d)
a = []
for j in d.values():
    if j not in a:
        a.append(j)
    else:
        print("we find")
