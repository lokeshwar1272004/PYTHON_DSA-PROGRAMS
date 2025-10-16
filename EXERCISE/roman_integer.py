d = {'I': 1,'V': 5,'L': 50,'C': 100,'D': 500,'M': 1000}
def method(s):
    n = 0
    for i in range(len(s)):
        if i+1 < len(s) and d[s[i]] < d[s[i+1]]:

            n -=d[s[i]]
        else:
            n+=d[s[i]]
    return n

s = input().upper()
print(method(s))
