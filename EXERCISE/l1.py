list =['flw','fl','fl']
def lon(list):
    res = ''
    for i in range(len(list[0])):#3
        for s in list[1:]:#flow
            if i == len(s) or s[i]!=list[0][i]:#'f'
                return res
        res+=list[0][i]
    return res
print(lon(list))