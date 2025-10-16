class bubble_short:
    def bubble(self,number,key=None):
        number = number
        n = len(number)-1

        for i in range(n):
            for j in range(n):
                swapped = False
                a = number[j][key]
                b = number[j+1][key]
                if a > b:
                    temp = number[j]
                    number[j] = number[j+1]
                    number[j+1]=temp
                    Swapped = True
            if not Swapped:
               break





number=[
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble = bubble_short()
bubble.bubble(number,key='name')
print(number)

e=[8,0,1,2]
m=len(e)-1
for i in range(m):
    for j in range(m-i):
        if e[j] > e[j+1]:
            temp = e[j]
            e[j]=e[j+1]
            e[j+1]=temp
print(e)
