elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

keys = input()
if keys == 'name':
    print(elements[0])


def isValid(s):
    stack = []
    d = {'(': ')', '[': ']', '{': '}'}
    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            if stack==[]:
                return 0

            else:
                if d[stack[-1]] == i:
                    stack.pop()
                else:
                    return 0

    if stack == []:
        return 1
    else:
        return 0
s=input()
print(isValid(s))

