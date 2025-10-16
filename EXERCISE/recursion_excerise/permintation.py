def permutation(word):
    if len(word)==1:
        return [word]
    perms = permutation(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char +perm[i:])
    return result
print(permutation('abc'))

def permin(text):
    if len(text)==1:
        return text
    rec = permutation(text[1:])
    new=text[0]
    result=[]
    for i in rec:
        for j in range(len(i)+1):
            result.append(i[:j]+new+i[j:])
    return result
print(permin('abc'))


