element = [0,0,0,1,1,1,1,2,3,3]
i = 0
j = 2
while i < len(element) and j < len(element):
    if element[i]== element[j]:
        element.pop(i)
    else:
        i+=1
        j=i+2

print(element)