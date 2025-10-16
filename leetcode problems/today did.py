haystack ="l"
needle ="l"
count=0
index=0
i=0
while i < len(needle):
    for j in range(len(haystack)):
        if i <len(needle) and needle[i]==haystack[j]:
            i+=1
            if i == len(needle):
               i+=-1
               index = j-i
               print("..",index)
               count += 1
               i = 0
        else:
            i=0
    break

print(count)
