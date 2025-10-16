class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        lisr =''
        while itr:
            lisr += str(itr.data) +'-->>'
            itr = itr.next
        print(lisr)

    def indert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_some_values(self,data_list):
        for data_values in data_list:
            self.indert_at_end(data_values)

    def get_length_list(self):
        itr = self.head
        count = 0
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index<0 or index >=self.get_length_list():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index<0 or index> self.get_length_list():
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def leetcode_index(self):
        dummy=Node()
        dummy.next=self.head



if __name__=='__main__':
    linked = Linked_list()
    linked.insert_at_begining(1)
    linked.insert_at_begining(2)
    linked.indert_at_end(3)
    linked.print()
    print("the total count linked list is",linked.get_length_list())
    print('............................................******')
linked = Linked_list()
linked.insert_some_values(["banana","orange","grape","lotus"])
linked.print()
linked.remove_at(2)
linked.print()
linked.insert_at(2,"dark_evil")
linked.print()


print('....................................')
linked.print()

