class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):  # returns current level of the tree
        level = 0
        p = self.parent
        while p:  # while parent exist
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""  # only add |__ if parent exist
        print(prefix + self.data)  # ..(1)
        if self.children:  # if children exist for that data
            for child in self.children:  # it will call print_tree & print the child in the call at eqn (1) & then the
                child.print_tree()  # call will check if its children exists & if exists call again print_tree

    def add_child(self, child):
        child.parent = self  # self is the parent
        self.children.append(child)


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('iPhone'))  # laptop will be the self parameter
    laptop.add_child(TreeNode('Pixel'))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


if __name__ == '__main__':
    build_product_tree()
