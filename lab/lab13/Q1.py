# 1. Given an undirected Graph (V, E), in Adjacency Matrix,
# generate its Adjacency Lists,
# using it to calculate and print out degree(i)


def adjacency_matrix_to_adjacency_lists_and_degree(matrix):
    n = len(matrix)
    degrees = [0]*n
    adlist = [[] for m in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                degrees[i] += 1
                degrees[j] += 1
                adlist[i].append(j)
    return adlist, degrees


matrix = [[0, 1, 0, 1, 1],
          [1, 0, 1, 0, 0],
          [0, 1, 0, 0, 0],
          [1, 0, 0, 1, 1],
          [1, 0, 0, 1, 0]]
al, degree = adjacency_matrix_to_adjacency_lists_and_degree(matrix)
print("adjacency_lists: ")
for j in range(len(al)):
    print(str(j)+" --> "+str(al[j])[1:-1])
print("\ndegree(i):")
for i in range(len(degree)):
    print("i = "+str(i)+" : "+str(degree[i]))