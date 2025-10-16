def valid(s):
    stack = []
    d = {'(':')','[':']','{':'}'}
    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            if stack==[]:
                return False
            else:
                if d[stack[-1]]==i:
                    stack.pop()

    if stack==[]:
        return True
    else:
        return False


s = input()
print(valid(s))