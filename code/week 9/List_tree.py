class list_tree:

    def __init__(self):
        self.tree = {}

    def show_tree(self):
        level = [self.root]
        while len(level) != 0:
            print(level)
            temp = []
            for item in level:
                temp += self.tree[item]
            level = temp

    def set_root(self, root):
        self.tree[root] = []
        self.root = root

    def add_as_next(self, node, *value):
        for val in value:
            self.tree[node].append(val)
            self.tree[val] = []


Tree = list_tree()
Tree.set_root("A")
Tree.add_as_next("A", "B", "C", "D")
Tree.add_as_next("B", "E", "F")
Tree.add_as_next("C", "G")
Tree.add_as_next("D", "H", "I", "J")
Tree.add_as_next("E", "K", "L")
Tree.add_as_next("H", "M")

print(Tree.tree)
Tree.show_tree()



