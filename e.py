number = [0,1,0,3,2]
i = 0
j = 0
while j<len(number):
    j+=1
    if number[i]!=0:
        i+=1

    if j < len(number) and number[j]!=0:
        number[j],number[i]=number[i],number[j]


print(number)

n = number
i = len(number)-1
j = len(number)-1
while j>=0:
    j-=1
    if n[i]!=0:
        i-=1
    if j>=0 and n[j]!=0:
        n[j],n[i]=n[i],n[j]
print(n)

