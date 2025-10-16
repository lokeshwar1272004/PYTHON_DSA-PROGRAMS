def move(input_str):
    uppercase_letters= ""
    remaining_letters= ""
    for char in input_str:
        if char.isupper():
            uppercase_letters+=char
        else:
            remaining_letters+=char
    rearanged_str=remaining_letters+uppercase_letters
    return rearanged_str
input_str=input("enter")
result=move(input_str)
print(result)


def charcter(words):
    ul=''
    ll=''
    for i in words:
        if i.isupper():
            ul+=i
        else:
            ll+=i
    orderl=ul+ll
    return orderl

print(charcter(input("enter your name or any thing")))




