class binary_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binary_tree(data)
        else:
            if data > self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = binary_tree(data)

    def inorder(self):
        element = []
        if self.left:
            element +=self.left.inorder()
        element.append(self.data)

        if self.right:
            element +=self.right.inorder()
        return element

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min = self.right.min()
            self.data = min
            self.right = self.right.delete(min)
        return self


    def minDepth(self):
        if not self:
            return 0
        if not self.left and not self.right:
            return 1
        if not self.right and self.left:
            return 1+self.left.minDepth()
        if not self.left and self.right:
            return 1+self.right.minDepth()
        return 1+min(self.right.minDepth(),self.left.minDepth())


    def min(self):
        if self.left:
            return self.right.min()
        return self.data

elements = [3,9,20,15,7]
root = binary_tree(elements[0])
for i in range(1,len(elements)):
    root.add_child(elements[i])
print(root.inorder())
print(root.minDepth())

#leaf = 0
#print(root.short(count,leaf=1))
