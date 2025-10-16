class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None
head =Node(1)
node2 = Node(2)
node3 = Node(3)
head.pointer = node2
node2.pointer = node3

current_node = head

while (current_node is not None):
    print(current_node.data)
    current_node = current_node.pointer


