# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.children = []
#         self.parent = None  

#     def add_child(self, child_node):
#         self.children.append(child_node)
        
#     def __str__(self):
#         return str(self.val)
    
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent

#         return level
    
#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|_" if self.parent else ""
#         print(prefix + self.val)
#         if len(self.children):
#             for child in self.children:
#                 child.print_tree()
    
# if __name__ == "__main__":
#     # Create the root node
#     root = TreeNode("A")

#     # Create child nodes
#     B = TreeNode("B")
#     C = TreeNode("C")
#     D = TreeNode("D")
#     E = TreeNode("E")

#     # Add child nodes to the root node
#     root.add_child(B)
#     root.add_child(C)

#     # Add child nodes to the B node
#     B.add_child(D)
#     B.add_child(E)

#     root.print_tree()

    
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
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