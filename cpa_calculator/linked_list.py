class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_node(self,data):
        node=Node(data,self.head)
        self.head=node
    def print_link(self):
        itr=self.head
        lis = ''
        reverse=''
        while itr:
            lis+=str(itr.data)+'-->'
            itr=itr.next
        return lis

    def insert_end(self,data):
        if self.head is None:
            Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def total_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count


    def leetcode(self):
        total_size=l.total_length()
        """last = self.head
        first = self.head
        length = total_size//2
        stack = []
        while length:
            last=last.next
            length-=1

        temp=last.next
        last.next=None
        while temp:
            stack.append(temp)
            temp=temp.next
        while first and stack:
            og=first.next
            first.next=stack.pop()
            first=first.next
            first.next=og
            first=first.next"""
        itr = self.head
        count = 0
        stack = []
        first = self.head
        last = self.head
        while itr:
            count += 1
            itr = itr.next
        length = count // 2
        while length:
            length -= 1
            last = last.next

        temp = last.next
        last.next = None
        while temp:
            stack.append(temp)
            temp = temp.next
        while stack and first:
            og = first.next
            first.next = stack.pop()
            first= first.next
            first.next= og
            first= first.next
        return self.head

    def leetcode_p1(self,n):
        total_size = l.total_length()
        dummy=Node()
        dummy.next=self.head
        itr=dummy
        while itr:
            if total_size==n:
                if itr.next.next:
                    itr.next=itr.next.next
                else:
                    itr.next=None
            total_size -= 1
            itr=itr.next
        self.head=dummy.next
        return self.head





if __name__== '__main__':
    l = Linked_list()
    l.insert_node(2)
    l.insert_end(4)
    l.insert_end(6)
    l.insert_end(8)


    l.leetcode_p1(2)
    print(l.print_link())
    #l.leetcode()

    print(l.print_link())



