# 2. Given a directed Graph (V, E), in Adjacency Matrix,
# generate its MultLists,
# using it to calculate and print out degree(i)


class multi_list():
    def __init__(self):
        self.data = {}

    def set(self, i, j, value):
        if i in self.data.keys():
            self.data[i][j] = value
        else:
            self.data[i] = {}
            self.data[i][j] = value

    def get(self, i, j):
        return self.data[i][j]


def adjacency_matrix_to_multlists(matrix):
    n = len (matrix)
    multilist = multi_list()
    for i in range (n):
        for j in range (n):
            if matrix[i][j] == 1:
                multilist.set(i,j,1)
    return multilist


def multilist_to_degrees(mlist,n):
    degree = [0]*n
    for i, j_value in mlist.data.items():
        for j in j_value.keys():
            degree[i] += 1
            degree[j] += 1
    return degree


matrix = [[0, 1, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0],
          [1, 0, 0, 1, 0],
          [1, 0, 0, 1, 0]]

multilist = adjacency_matrix_to_multlists(matrix)

print(multilist.data)
degree = multilist_to_degrees(multilist, len(matrix))

print("edges:")
for i, j_value in multilist.data.items ():
    for j in j_value.keys ():
        print(str(i)+"-->"+str(j))

print("\ndegree(i):")
for i in range(len(degree)):
    print("i = "+str(i)+" : "+str(degree[i]))