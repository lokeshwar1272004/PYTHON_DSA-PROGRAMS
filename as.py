s = "abcabcbb"
char=set()
l=0
maximum=0
for i in range(len(s)):
    while s[i] in char:
        char.remove(s[i])
        l+=1
    char.add(s[i])
    maximum=max(maximum,i-l+1)

print(maximum)