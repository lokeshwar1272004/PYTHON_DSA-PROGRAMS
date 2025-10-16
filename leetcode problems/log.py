dictonery ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
"ruels grater to small + otherwise -"
character = 'III'
def roman_integer(character):
    result = 0
    i = 0
    while i < len(character):
        if i+1 < len(character) and dictonery[character[i]]< dictonery[character[i+1]]:
            result-=dictonery[character[i]]
            i+=1
        else:
            result+=dictonery[character[i]]
            i+=1

    return result

print(roman_integer(character))