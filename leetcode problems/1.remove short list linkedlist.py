class Node():
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class linked_list():
    def __init__(self):
        self.head=None
    def add(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
           self.head=Node(data,None)
           return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def printin(self):
        if self.head is None:
            return "ll"
        cur = self.head
        itr=''
        while cur:
            itr+=str(cur.val)+"..>"
            cur=cur.next
        return itr
    def remmove_duplicte(self):
        cur=self.head
        while cur:
            while cur.next and cur.val==cur.next.val:
                cur.next=cur.next.next
            cur=cur.next
        return cur







l=linked_list()
l.insert_at_end(1)
l.insert_at_end(1)
l.insert_at_end(2)
l.insert_at_end(2)
l.insert_at_end(3)
l.insert_at_end(4)

l.remmove_duplicte()
print(l.printin())




