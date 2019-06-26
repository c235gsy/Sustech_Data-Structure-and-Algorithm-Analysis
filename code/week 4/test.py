class Demo:
    id = 123456

    def getId(self):
        return self.__id

temp = Demo()
# print(temp.__id)  # 报错 AttributeError: 'Demo' object has no attribute '__id'
print(temp.getId())  # 123456
print(temp._Demo__id)  # 123456