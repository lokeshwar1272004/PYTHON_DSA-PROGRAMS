class Hash_Tabble:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h +=ord(char)
        return h % self.MAX
    def __setitem__(self,key,val): #t.add()
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] =None,"its delete"

"""t = Hash_Tabble()
t.add('march 6',130)
t.add('july 7',7)
print(t.get('march 6'))
t.deli('july 7')
print(t.get('july 7'))"""


t = Hash_Tabble()
t['march 6'] = 130
t['may 4'] = 420
t['march 6'] = 127
t['march 17']=777
print(t['march 6'])
print(t['may 4'])
del t['may 4']
print(t['may 4'])
print(t['march 17'])