s ='([)'
d = {'(': ')', '[': ']', '{': '}'}
stack = []
for i in s:
    if i in d.keys():
        stack.append(i)
    else:
        if stack == []:
            print(False)

        if d[stack[-1]] == i:
            stack.pop()

if stack == []:
    print(True)
else:
    print(False)

