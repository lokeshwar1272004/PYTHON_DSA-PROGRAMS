class binary:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def create(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.create(data)
            else:
                self.left = binary(data)
        else:
            if self.right:
                self.right.create(data)
            else:
                self.right = binary(data)

    def inorder(self):
        N_element = []
        if self.left:
            N_element +=self.left.inorder()
        N_element.append(self.data)

        if self.right:
            N_element+=self.right.inorder()
        return N_element

    def pre_order(self):
        p_element =[]
        p_element.append(self.data)
        if self.left:
            p_element+=self.left.pre_order()


        if self.right:
            p_element+=self.right.pre_order()
        return p_element

    def minimum(self):
        if self.left:
            return self.left.minimum()
        return self.data
    def maximum(self):
        if self.right:
            return self.right.maximum()
        return self.data

elements = [3,2,1,4]

def bulit():
    for i in range(1, len(elements)):
        obj.create(elements[i])
    return obj
obj = binary(elements[0])
bulit()

print("inorder: ",obj.inorder())
print("max: ",obj.minimum())
print("min ",obj.maximum())

