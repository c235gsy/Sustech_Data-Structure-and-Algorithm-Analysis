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
        global output_level
        output_level = []
        self.__levelorder([self.root])
        return output_level

    def __levelorder(self, nodes):
        if nodes == []:
            return
        sons = []
        for node in nodes:
            output_level.append(node.value)
            son = node.first_child
            while son:
                sons.append(son)
                son = son.next_sibling
        self.__levelorder(sons)

    def __preorder(self, node):
        output_pre.append(node.value)
        son = node.first_child
        if son:
            while son.next_sibling:
                self.__preorder(son)
                son = son.next_sibling
            self.__preorder(son)

    def preorder_traversal(self):
        global output_pre
        output_pre = []
        self.__preorder(self.root)
        return output_pre

    def __inorder(self, node):
        son = node.first_child
        if son:
            self.__inorder (son)
            output_in.append (node.value)
            while son.next_sibling:
                son = son.next_sibling
                self.__inorder(son)
        else:
            output_in.append(node.value)

    def inoder_traversal(self):
        global output_in
        output_in = []
        self.__inorder(self.root)
        return output_in

    def __postorder(self, node):
        son = node.first_child
        if son:
            while son.next_sibling:
                self.__postorder (son)
                son = son.next_sibling
            self.__postorder(son)
        output_post.append(node.value)

    def postorder_traversal(self):
        global output_post
        output_post = []
        self.__postorder(self.root)
        return output_post


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

print(Tree.levelorder_traversal())
print(Tree.preorder_traversal())
print(Tree.inoder_traversal())
print(Tree.postorder_traversal())


tree = FCNS_tree()
tree.set_root("D")
tree.add_as_first_child("D", "B")
tree.add_as_next_sibling("B", "F")
tree.add_as_first_child("B", "A")
tree.add_as_first_child("F", "E")
tree.add_as_next_sibling("A", "C")
tree.add_as_next_sibling("E", "G")
tree.show()
print("levelorder: "+str(tree.levelorder_traversal()))
print("preorder"+str(tree.preorder_traversal()))
print("inorder"+str(tree.inoder_traversal()))
print("postorder"+str(tree.postorder_traversal()))





