
class Node:
    def __init__(self, value, front_node, next_node):
        self.val = value
        self.front = front_node
        self.next = next_node

    def set_value(self, v):
        self.val = v

    def set_front_node(self, f):
        self.front = f

    def set_next_node(self, n):
        self.next = n


class Pylist:

    def __init__(self, *nodes):
        self.limit_mark = 0
        self.the_size = 0

        for n in nodes:
            new_node = Node (n, str (self.limit_mark - 1), str (self.limit_mark + 1))
            setattr (self, str (self.limit_mark), new_node)
            self.the_size += 1
            self.limit_mark += 1

        if hasattr (self, str (0)):
            self.first_index = str (0)
            getattr (self, self.first_index).set_front_node (None)

        if hasattr (self, str (self.the_size - 1)):
            self.last_index = str (self.the_size - 1)
            getattr (self, self.last_index).set_next_node (None)

    def __str__(self):
        string = ""
        the_node = getattr (self, self.first_index)
        while the_node.next is not None:
            string = string + str (the_node.val) + ","
            the_node = getattr (self, the_node.next)
        string = string + str (the_node.val)
        return string

    def get_node_at_point(self, point):
        index = 0
        the_node = getattr (self, self.first_index)
        while index < point:
            next_index = the_node.next
            the_node = getattr (self, next_index)
            index += 1
        return the_node

    def point_value(self, point):
        the_node = self.get_node_at_point (point)
        return the_node.val

    def set_value(self, point, new_value):
        self.get_node_at_point (point).set_value (new_value)

    def size(self):
        return self.the_size

    def first(self):
        return getattr (self, self.first_index).val

    def last(self):
        return getattr (self, self.last_index).val

    def insert_as_first(self, element):
        if self.the_size == 0:
            self.the_size = 1
            self.first_index = str(self.limit_mark)
            self.last_index = str(self.limit_mark)
            setattr(self,str(self.limit_mark),Node(element,None,None))
            self.limit_mark += 1
            return
        if self.the_size >= 1:
            getattr (self, self.first_index).set_front_node (str (self.limit_mark))
            new_node = Node (element, None, self.first_index)
            self.first_index = str (self.limit_mark)
            setattr (self, self.first_index, new_node)
            self.the_size += 1
            self.limit_mark += 1

    def insert_as_last(self, element):
        if self.the_size == 0:
            self.the_size = 1
            self.first_index = str (self.limit_mark)
            self.last_index = str (self.limit_mark)
            setattr(self,str(self.limit_mark),Node(element,None,None))
            self.limit_mark += 1
            return
        if self.the_size >= 1:
            getattr (self, self.last_index).set_next_node (str (self.limit_mark))
            new_node = Node (element, self.last_index, None)
            self.last_index = str (self.limit_mark)
            setattr (self, self.last_index, new_node)
            self.the_size += 1
            self.limit_mark += 1

    def insertA(self, point, element):
        if self.the_size == 0:
            print("the list is empty! And a new Node is added. ")
            self.the_size = 1
            self.first_index = str (self.limit_mark)
            self.last_index = str (self.limit_mark)
            setattr(self,str(self.limit_mark),Node(element,None,None))
            self.limit_mark += 1
            return
        if self.the_size >= 1:
            if point >= self.the_size or point < 0:
                print ("the index out of range!")
            if point == 0:
                self.insert_as_first (element)
            else:
                the_node = self.get_node_at_point (point)
                front_node = getattr (self, the_node.front)
                setattr (self, str (self.limit_mark), Node (element, the_node.front, front_node.next))
                front_index = the_node.front
                the_index = front_node.next
                getattr (self, front_index).set_next_node (str (self.limit_mark))
                getattr (self, the_index).set_front_node (str (self.limit_mark))
                self.the_size += 1
                self.limit_mark += 1

    def insertB(self, point, element):
        if self.the_size == 0:
            print ("the list is empty! And a new Node is added. ")
            self.the_size = 1
            self.first_index = str (self.limit_mark)
            self.last_index = str (self.limit_mark)
            setattr(self,str(self.limit_mark),Node(element,None,None))
            self.limit_mark += 1
            return
        if self.the_size >= 1:
            if point >= self.the_size or point < 0:
                print ("the index out of range!")
            if point == self.the_size - 1:
                self.insert_as_last (element)
            else:
                the_node = self.get_node_at_point (point)
                next_node = getattr (self, the_node.next)
                setattr (self, str (self.limit_mark), Node (element, next_node.front, the_node.next))
                next_index = the_node.next
                the_index = next_node.front
                getattr (self, next_index).set_front_node (str (self.limit_mark))
                getattr (self, the_index).set_next_node (str (self.limit_mark))
                self.the_size += 1
                self.limit_mark += 1

    def remove(self, point):
        if self.the_size == 0:
            print ("the list is empty!")
        if self.the_size == 1:
            if point == 0:
                value = self.get_node_at_point (0).val
                self.__init__ ()
                return value
        if self.the_size >= 2:
            if point >= self.the_size or point < 0:
                print ("the index out of range!")
            if point == 0:
                the_node = self.get_node_at_point (point)
                next_index = the_node.next
                the_node_index = getattr (self, next_index).front
                getattr (self, next_index).set_front_node (None)
                delattr (self, the_node_index)
                self.first_index = next_index
                self.the_size -= 1
                return the_node.val
            if point == self.the_size - 1:
                the_node = self.get_node_at_point (point)
                front_index = the_node.front
                the_node_index = getattr (self, front_index).next
                getattr (self, front_index).set_next_node (None)
                delattr (self, the_node_index)
                self.last_index = front_index
                self.the_size -= 1
                return the_node.val
            else:
                the_node = self.get_node_at_point (point)
                next_index = the_node.next
                front_index = the_node.front
                the_node_index = getattr (self, next_index).front
                getattr (self, next_index).set_front_node (front_index)
                getattr (self, front_index).set_next_node (next_index)
                delattr (self, the_node_index)
                self.the_size -= 1
                return the_node.val

    def find(self, element):
        index = 0
        the_node = getattr (self, self.first_index)
        result = False
        while the_node.next is not None:
            value = the_node.val
            if value == element:
                result = index
            index += 1
            the_node = getattr (self, the_node.next)
        return result

    def disordered(self):
        result = True
        for i in range (0, self.the_size - 1):
            the_node = self.get_node_at_point (i)
            the_value = the_node.val
            other_node = getattr (self, the_node.next)
            other_value = other_node.val
            if the_value > other_value:
                result = False
                break
            while other_node.next is not None:
                other_node = getattr (self, other_node.next)
                other_value = other_node.val
                if the_value > other_value:
                    result = False
                    break
        return result

    def find_the_min(self):
        if self.the_size == 0:
            print ("the list is empty!")
        else:
            index = 0
            the_node = getattr (self, self.first_index)
            minvalue = the_node.val
            minindex = 0
            while the_node.next is not None:
                the_node = getattr (self, the_node.next)
                value = the_node.val
                index += 1
                if minvalue > value:
                    minvalue = value
                    minindex = index
            value = the_node.val
            index += 1
            if minvalue > value:
                minvalue = value
                minindex = index
            return minindex

    def sort(self):
        if self.the_size == 0:
            print ("the list is empty!")
        if self.the_size == 1:
            print ("Cannot sort!!")
        else:
            sorted_pylist = Pylist ()
            while self.the_size != 0:
                minindex = self.find_the_min ()
                minvalue = self.remove (minindex)
                sorted_pylist.insert_as_last (minvalue)  # print(str(sorted_pylist))  # print(str(self))

            sorted_node = getattr (sorted_pylist, sorted_pylist.first_index)
            # print (str (sorted_pylist))
            while sorted_node.next is not None:
                self.insert_as_last (sorted_node.val)
                sorted_node = getattr (sorted_pylist, sorted_node.next)
            self.insert_as_last (sorted_node.val)


exsample = Pylist(0,1,2,3,4,5,6,7,8,10,9)

print(str(exsample))
print(exsample.size())
print(exsample.first())
print(exsample.last())

exsample.insert_as_first(100)
print(str(exsample))

exsample.insert_as_last(200)
print(str(exsample))

exsample.insertA(4,300)
print(str(exsample))

exsample.insertB(7,400)
print(str(exsample))

print(exsample.remove(7))

print(str(exsample))

print(exsample.disordered())
exsample.sort()
print(str(exsample))
print(exsample.disordered())

print(exsample.find(100))
print(exsample.find(700))