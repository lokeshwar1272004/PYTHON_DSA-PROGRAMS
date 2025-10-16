def longlest_comman_pr(character):
    result = ''
    for i in range(len(character[0])):
        for j in character[1:]:
            if i==len(j) or character[0][i]!=j[i]:
                return result
        result+=character[0][i]
    return result
character=["flower","flow","flight"]
print(longlest_comman_pr(character))
