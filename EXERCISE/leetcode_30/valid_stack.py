def valid_stack(n):  #()
    n = n
    stack = []
    d = {'[':']','(':')','{':'}'}
    for i in n:
        if i in d.keys():
            stack.append(i)
        else:
            if stack == []:
                return False

            else:
                if d[stack[-1]] == i:
                    stack.pop()
    if stack == []:
        return True
    else:
        return False



print(valid_stack('()('))