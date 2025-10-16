s='babad'
res=0
ans=''
for i in range(len(s)):
    l=r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>res:
            ans=s[l:r+1]
            res=r-l+1
        l-=1
        r+=1
print(ans)