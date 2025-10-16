class TreeNode:
    def __init__(self,data,work=None):
        self.data = data
        self.work = work
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level
    def print_tree(self,w):
        space = ' ' * self.get_level() * 3
        prefix = space + "<--" if self.parent else ""
        if w == 'name':
           print(prefix + self.data)
        elif w == 'work':
            print(prefix + self.work)
        else:
            print(prefix +self.data , self.work)




        if self.children:
            for child in self.children:
                child.print_tree(w)
def build_product_tree():
    root = TreeNode('Nilupul','CEO')
    E1 = TreeNode("chimay",'CTO')
    E2 = TreeNode('visway','interface HEAD')
    E2.add_child(TreeNode('dhaval','app manager'))
    E2.add_child(TreeNode('abhijith', 'cloud manager'))

    e2 = TreeNode('Amair','application manager')
    e1  = TreeNode('GELS','HR HEAD')
    e1.add_child(TreeNode('peter','recruitment manager'))
    e1.add_child(TreeNode('waqas','policy manager'))




    root.add_child(E1)
    E1.add_child(E2)
    E1.add_child(e2)
    root.add_child(e1)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree("name")
    print(".........222.")
    root.print_tree('work')
    print(".....12.12.12........................")
    root.print_tree('wo')

    #print(root.get_level())
    pass