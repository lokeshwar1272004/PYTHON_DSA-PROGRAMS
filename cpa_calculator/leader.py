arr = [16,17,4,3,5,2]

m=[]


for i in range(len(arr)):
    if i == len(arr) - 1:
        m.append(arr[i])

    elif arr[i]>(max(arr[i+1:])):
        m.append(arr[i])

print(m)
