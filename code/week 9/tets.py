class people(object):

    def __init__(self):
        self.name = "name"
        self.age = 99
        self.money = 50


class gourp(object):

    def __init__(self):
        self.head = people()

    def nnn(self):
        n = [self.head]
        for m in n:
            m.age = 0


ggg = gourp()
print(ggg.head.age)
ggg.nnn()
print(ggg.head.age)