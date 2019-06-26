class linked_node(object):

    def __init__(self, value=None):
        self.value = value
        self.next = []


class linked_list_tree(object):

    def __init__(self, value=None):
        self.root = linked_node(value)

    def add_as_child(self, father, *child):
        current_level = [self.root]
        next_level = []
        while current_level != []:
            for node in current_level:
                if node.value == father:
                    node.next += list(map(linked_node, child))
                    return
                else:
                    next_level += node.next
            current_level = next_level
            next_level = []
        print("do not find father")

    def show(self, node=None):
        if not node:
            node = self.root
        print(node.value,end=" ")
        nodes = node.next
        for no in nodes:
            self.show(no)


Tree = linked_list_tree("A")
Tree.add_as_child("A", "B", "C", "D")
Tree.add_as_child("B", "E", "F")
Tree.add_as_child("E", "K", "L")
Tree.add_as_child("C", "G")
Tree.add_as_child("D", "H", "I", "J")
Tree.add_as_child("H", "M")
Tree.show()

"""
level: A B C D E F G H I J K L M 
pre:   A B E K L F C G D H M I J 
in:    K E L B F A G C M H D I J 
post:  K L E F B G C M H I J D A 

"""
