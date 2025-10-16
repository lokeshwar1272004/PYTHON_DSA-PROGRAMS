class Node:
    def __init__(self,data):
        self.data = data
        self.pointer=None

class linked_list:
    def __init__(self):
        self.head = None

    def add(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while(cur.pointer):
                cur = cur.pointer
            cur.pointer = newNode

    def print(self):
        cur = self.head

        while(cur is not None):
            print(cur.data,end='..>')
            cur = cur.pointer


    def remove(self,data):
        if(self.head is not None):
            if(self.head.data == data):
                self.head = self.head.pointer

            else:
                cur = self.head
                while(cur.pointer is not None and cur.pointer.data!=data):
                    cur= cur.pointer
                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
                else:
                    print("is not not present in linkedlist")





linkedlist = linked_list()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist.add(4)
linkedlist.add(5)
linkedlist.print()
print('..next...')

linkedlist.remove(3)
linkedlist.print()