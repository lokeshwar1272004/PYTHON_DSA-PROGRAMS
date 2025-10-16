class Node:
    def __init__(self,pre=None,data=None,next=None):
        self.pre = pre
        self.data = data
        self.next = next

class Double_linked_list:
    def print_forward(self):
        if self.head is None:
            print("list_empty")
            return
        itr = self.head
        ldata = ''
        while itr:
            ldata+= str(itr.data) + "-->"
            itr = itr.next
        print(ldata)
        return


    def __init__(self):
        self.head = None

    def insert_beginning(self,data):
        if self.head == None:
            self.head=Node(None,data,self.head)

        else:
            node = Node(None,data,self.head)
            self.head.pre = node
            self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(None,data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next=Node(itr,data,None)

    def backward(self):
        if self.head is None:
            print("its empty")
            return
        get_last_node = self.last_Node()

        itr = get_last_node
        reverse = ''

        while itr:
            reverse+=str(itr.data)+"<---"
            itr = itr.pre
        print(reverse)
        return
    def last_Node(self):
        if self.head is None:
            print("its empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception ("invalid Index")
        if index-1==0:
            self.insert_beginning(data)
            return
        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                node = Node(itr,data,itr.next)
                if itr.next:
                    node.next.pre = node
                itr.next = node
                return
            itr = itr.next
            count+=1

    def insert_values(self,data):
        self.head = None
        for i in data:
            self.insert_at_end(i)

    def remove_at(self,index):
        if index < 0 and index > self.get_length():
            raise Exception ("invalid index")
        if index == 0:
            self.head.next = self.head
            self.head.next.pre = None
            return
        count = 0
        itr = self.head

        while itr:
            if index == count:
                    itr.pre.next = itr.next
                    if itr.next:
                        itr.next.pre = itr.pre
                    break
            itr = itr.next
            count+=1


dl = Double_linked_list()
list_values = ['apple','orange','banana','jack fruit']
dl.insert_values(list_values)
dl.print_forward()
dl.insert_at(2,'strawberry')
dl.backward()
dl.get_length()
dl.remove_at(3)
dl.print_forward()
