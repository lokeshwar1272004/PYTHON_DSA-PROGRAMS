s ='dvdf'
i = j = 0
char = ''
max_char = 0
while j < len(s):
    if s[j] not in char:
        char += s[j]

    else:
        if (j - i + 1) - 1 > max_char:
            max_char = (j - i + 1) - 1
        char = s[j]
        i = j
    j += 1

if max_char==0 or j-i:
    max_char = j-i
print(max_char)

a = '     '
if a:
    len(a)