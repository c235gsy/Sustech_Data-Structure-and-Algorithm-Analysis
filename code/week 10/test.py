class BST_node ():

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value


## 左最大找右边，右最小找左边


class BST_tree ():

    def __init__(self, value=None):
        self.head = BST_node (value)

    def is_empty(self):
        if not self.head.value:
            return True
        else:
            return False

    def insert(self, value):
        if self.is_empty ():
            self.head.value = value
        else:
            current_node = self.head
            while True:
                if current_node.value < value:
                    if current_node.right == None:
                        current_node.right = BST_node (value)
                        return
                    else:
                        current_node = current_node.right

                else:
                    if current_node.left == None:
                        current_node.left = BST_node (value)
                        return
                    else:
                        current_node = current_node.left

    def delete(self, value):
        father_node = None
        current_node = self.head
        flag = None
        while True:
            if current_node.value < value:
                if current_node.right == None:
                    return
                else:
                    father_node = current_node
                    flag = "right"
                    current_node = current_node.right

            elif current_node.value > value:
                if current_node.left == None:
                    return
                else:
                    father_node = current_node
                    flag = "left"
                    current_node = current_node.left

            elif current_node.value == value:
                break

        if flag == "right":
            if current_node.right == None and current_node.left == None:
                father_node.right = None

            elif current_node.right != None and current_node.left == None:
                father_node.right = current_node.right

            elif current_node.right == None and current_node.left != None:
                father_node.right = current_node.left

            elif current_node.right != None and current_node.left != None:
                point = current_node.right
                while point.left != None:
                    point = point.left
                temp = point.value
                self.delete(point.value)
                current_node.value = temp

        if flag == "left":
            if current_node.right == None and current_node.left == None:
                father_node.left = None

            elif current_node.right != None and current_node.left == None:
                father_node.left = current_node.right

            elif current_node.right == None and current_node.left != None:
                father_node.left = current_node.left

            elif current_node.right != None and current_node.left != None:
                point = current_node.right
                while point.left != None:
                    point = point.left
                temp = point.value
                self.delete (point.value)
                current_node.value = temp

    def show(self):
        current_level = [self.head]
        next_level = []
        while current_level != []:
            for node in current_level:
                if node.left:
                    next_level.append (node.left)
                if node.right:
                    next_level.append (node.right)
            print (list (map (BST_node.get_value, current_level)))
            current_level = next_level
            next_level = []


BBB = BST_tree ()
bbb = BST_tree ()
for i in range (8):
    # print(i)
    BBB.insert (value=i)

for p in [4, 2, 1, 3, 6, 5, 7]:
    bbb.insert (value=p)

bbb.show ()
print ()
bbb.delete (6)
bbb.show ()
print ()
BBB.show ()
print ()
BBB.delete (6)
BBB.show ()