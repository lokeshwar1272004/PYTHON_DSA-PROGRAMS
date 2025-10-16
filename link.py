class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)

        self.head = node

    def prin(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head

        llistr=''

        while itr:
            llistr +=str(itr.data)+'__'
            itr=itr.next
        print(llistr)

    def insertat_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

if __name__ =='__main__':
    ll=Linked_list()
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insertat_end(4)
    ll.prin()




