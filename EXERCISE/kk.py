class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class linked_list:
    def __init__(self):
        self.head =None
    def insert(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            return False
        itr = self.head
        lis=''
        while itr:
            lis+=str(itr.data)+'__>'
            itr=itr.next
        return lis


k=linked_list()
k.insert(1)
k.insert(2)
k.insert(3)

print(k.print())