haystack = "sadbutsad"
needle ="sad"
if needle == '':
    print(0)
else:
    for i in range(len(haystack)+1 - len(needle)):
        if haystack[i:i+len(needle)]==needle:
            print(1)