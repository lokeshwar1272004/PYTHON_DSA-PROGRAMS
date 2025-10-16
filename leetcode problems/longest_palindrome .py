string = 'babad'
res = ''
res_len=0

for i in range(len(string)):
    #odd_length_string
    l=r=i
    while l>=0 and r<len(string) and string[l]==string[r]:
        res=string[l:r+1]
        res_len=max(r-l+1,res_len)
        l-=1
        r+=1

    #even_length_string
    l,r=i,i+1
    while l>=0 and r<len(string) and string[l]==string[r]:
        res=string[l:r+1]
        res_len=max(r-l+1,res_len)
        l=-1
        r+=1
print(res_len)
print(res)