class Hash_Tabble:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h +=ord(char)
        return h % self.MAX
    def __setitem__(self,key,val): #t.add()
        h = self.get_hash(key)
        found =False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))



    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] ==key:
                del self.arr[h][index]


t = Hash_Tabble()
t['march 6'] = 130
t['may 4'] = 420
t['march 6'] = 127
t['march 17']=777
print(t['march 6'])
print(t['may 4'])
print(t['march 6'])
del [t['march 17']]
print(t['march 17'])


