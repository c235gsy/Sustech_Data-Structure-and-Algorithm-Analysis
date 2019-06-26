class FCNS_node(object):

    def __init__(self, value, first_child=None, next_sibling=None):
        self.value = value
        self.first_child = first_child
        self.next_sibling = next_sibling


class FCNS_tree(object):

    def __init__(self):
        self.root = None

    def set_root(self, value, first_child=None, next_sibling=None):
        self.root = FCNS_node(value, first_child, next_sibling)

    def get_root(self):
        return self.root

    def add_as_first_child(self, node, value):
        current_level = [self.root]
        next_level = []
        while current_level:

            for current_node in current_level:
                if current_node.value == node:
                    if not current_node.first_child:
                        current_node.first_child = FCNS_node(value)
                        return
                    else:
                        print("this men has the first child")
                elif current_node.first_child:
                        point = current_node.first_child
                        while point.next_sibling:
                            next_level.append(point)
                            point = point.next_sibling
                        next_level.append(point)

            current_level = next_level
            next_level = []
        print("Do not find the node")

    def add_as_next_sibling(self, node, value):
        current_level = [self.root]
        next_level = []
        while current_level:

            for current_node in current_level:
                if current_node.value == node:
                    if not current_node.next_sibling:
                        current_node.next_sibling = FCNS_node(value)
                        return
                    else:
                        print ("this men has the next sibling")
                elif current_node.first_child:
                    point = current_node.first_child
                    while point.next_sibling:
                        next_level.append(point)
                        point = point.next_sibling
                    next_level.append (point)

            current_level = next_level
            next_level = []

    def show(self):
        current_level = [self.root]
        next_level = []
        while current_level:
            print()

            for current_node in current_level:
                print(current_node.value, end=" ")
                if current_node.first_child:
                    point = current_node.first_child
                    while point.next_sibling:
                        next_level.append(point)
                        point = point.next_sibling
                    next_level.append (point)

            current_level = next_level
            next_level = []
        print()

    def levelorder_traversal(self):
        current_level = [self.root]
        next_level = []

        while current_level:

            for current_node in current_level:
                print (current_node.value, end=" ")
                if current_node.first_child:
                    point = current_node.first_child
                    while point.next_sibling:
                        next_level.append(point)
                        point = point.next_sibling
                    next_level.append(point)

            current_level = next_level
            next_level = []
        print()

    def preorder_traversal(self, node=None):
        current = node
        if node == None:
            current = self.root
        print(current.value, end=" ")
        if current.first_child != None:
            p2 = current.first_child
            while p2.next_sibling != None:
                self.preorder_traversal(p2)
                p2 = p2.next_sibling
            self.preorder_traversal(p2)

    def inoder_traversal(self, node=None):
        current = node

        if node == None:
            current = self.root

        if current.first_child == None:
            print(current.value, end=" ")
            return

        if current.first_child.first_child == None:
            father1 = current
            son1 = current.first_child
            print(son1.value, end=" ")
            print(father1.value, end=" ")
            while son1.next_sibling != None:
                print(son1.next_sibling.value, end=" ")
                son1 = son1.next_sibling
            return

        else:
            father2 = current
            son2 = current.first_child
            self.inoder_traversal(son2)
            print(father2.value, end=" ")
            while son2.next_sibling != None:
                self.inoder_traversal(son2.next_sibling)
                son2 = son2.next_sibling

    def postorder_traversal(self, node=None):
        """done"""
        current = node

        if node == None:
            current = self.root

        if current.first_child == None:
            print(current.value, end=" ")
            return

        if current.first_child.first_child == None:
            father1 = current
            son1 = current.first_child
            print(son1.value, end=" ")
            while son1.next_sibling != None:
                print(son1.next_sibling.value, end=" ")
                son1 = son1.next_sibling
            print (father1.value, end=" ")
            return

        else:
            father2 = current
            son2 = current.first_child
            self.postorder_traversal(son2)
            while son2.next_sibling != None:
                self.postorder_traversal(son2.next_sibling)
                son2 = son2.next_sibling
            print(father2.value, end=" ")


Tree = FCNS_tree()
Tree.set_root("A")
Tree.add_as_first_child("A", "B")
Tree.add_as_next_sibling("B", "C")
Tree.add_as_next_sibling("C", "D")
Tree.add_as_first_child("B", "E")
Tree.add_as_next_sibling("E", "F")
Tree.add_as_first_child("E", "K")
Tree.add_as_next_sibling("K", "L")
Tree.add_as_first_child("C", "G")
Tree.add_as_first_child("D", "H")
Tree.add_as_next_sibling("H", "I")
Tree.add_as_next_sibling("I", "J")
Tree.add_as_first_child("H", "M")

Tree.show()
print()
Tree.levelorder_traversal()
print()
Tree.preorder_traversal()
print()
Tree.inoder_traversal()
print()
Tree.postorder_traversal()


"""

level: A B C D E F G H I J K L M 
pre:   A B E K L F C G D H M I J 
in:    K E L B F A G C M H D I J 
post:  K L E F B G C M H I J D A 

"""

tree = FCNS_tree()
tree.set_root("D")
tree.add_as_first_child("D", "B")
tree.add_as_next_sibling("B", "F")
tree.add_as_first_child("B", "A")
tree.add_as_first_child("F", "E")
tree.add_as_next_sibling("A", "C")
tree.add_as_next_sibling("E", "G")

print()
tree.show()
print()
tree.levelorder_traversal()
print()
tree.preorder_traversal()
print()
tree.inoder_traversal()
print()
tree.postorder_traversal()




