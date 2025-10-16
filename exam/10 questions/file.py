element = [2,2,3,4,5,6,7,7]
l = 1
for r in range(1,len(element)):
    if element[r]!=element[r-1]:
        element[l]=element[r]
        l+=1



print(l)
print(element)