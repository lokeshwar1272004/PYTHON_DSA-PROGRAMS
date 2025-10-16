n=[2,3,4,-1,2,1]
max_sub=n[0]
cur_sum=0
for i in n:
    if cur_sum<0:
        cur_sum=max(cur_sum,0)
    cur_sum+=i
    max_sub=max(cur_sum,max_sub)


print(cur_sum)