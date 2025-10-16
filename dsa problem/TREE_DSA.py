class TreeNode:
    def __init__(self,data):
        self.data = data
        self.childern = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.childern.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p=p.parent
        return level

    def print(self):
        space = ' ' * self.get_level() * 3
        prefix = space + '|__' if self.parent else""
        print(prefix + self.data)
        if self.childern:
            for child in self.childern:
                child.print()
def bulid_product_tree():
    root = TreeNode("Electronic")
    laptop = TreeNode("Laptop")

    root.add_child(laptop)


    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("cellphone")

    root.add_child(cellphone)

    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("android"))
    cellphone.add_child(TreeNode("vivo"))

    tv = TreeNode("tv")

    root.add_child(tv)

    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("hair"))



    return root

if __name__ =='__main__':
    root = bulid_product_tree()
    root.print()