arr = [-4,2,1,5]
sum_element = 0
i = 0
while i < len(arr):
    sum_element = arr[i]
    for j in range(i+1,len(arr)):
        if sum_element+arr[j]>sum_element:
            sum_element+=arr[j]
        else:
            sum_element-=arr[i]
            i+=1
    break

print(sum_element)
