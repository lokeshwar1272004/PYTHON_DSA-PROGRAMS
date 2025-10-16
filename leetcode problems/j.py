nums =[-1,1,0,0]
count=0
x=0
g_count=0
for i in nums:
    if i ==0:
        print(0)
        break
    if i < 0:
        a = 0
        if count == 0:
            a -= i
            count=a
        else:
            a-=i
            if a < count:
                count = a

    if i > 0:
        if g_count==0:
            g_count = i
        else:
            if i < g_count:
                g_count=i
if count==0:
    print(g_count)
if g_count==0:
    print(-count)
if count == g_count:
    print(g_count)
if count > g_count:
    print(g_count)
else:
    print(-count)






