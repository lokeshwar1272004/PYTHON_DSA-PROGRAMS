stack =[]
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2
def is_balanced(s):
    d=['[',']','(',')','{','}']
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.append(ch)
        if ch==')' or ch=='}' or ch == ']':
            if len(stack)==0:
                return False
            if not is_match(ch,stack.pop()):
                return False
        if ch not in d:
            return False



    if stack==[]:
        return True
    else:
        return False


s = input()
print(is_balanced(s))
