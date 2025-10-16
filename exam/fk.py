n ='mobile 100;tv 50;san 20'
a=n.split(';')
print(a)
d =0
ans=''
b= []
for i in a:
    b.append(i.split(' '))
for j,k in b:
    if int(k)>d:
        d=int(k)
        ans=j
print(ans)
