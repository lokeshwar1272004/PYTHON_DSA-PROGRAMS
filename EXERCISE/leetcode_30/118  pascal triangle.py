def pascal_triangle():
    result = [[1]]
    for i in range(4):
        temp =[]
        temp+=[0]+result[-1]+[0]
        row = []
        for j in range(len(result)+1):
            row.append(temp[j]+temp[j+1])
        result.append(row)
    print(result)
pascal_triangle()




