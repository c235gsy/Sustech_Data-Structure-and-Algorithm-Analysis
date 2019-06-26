
def Dijkstra(Graph,start,INF=999):
    booked_nodes = set()
    path = dict((k, []) for k in Graph.keys())
    min_node = start
    dis = dict((k, INF) for k in Graph.keys())
    dis[start] = 0
    path[start] = [start]
    while len(booked_nodes) < len(Graph):
        booked_nodes.add(min_node)
        for next_node in Graph[min_node]:
            if dis[min_node] + G[min_node][next_node] < dis[next_node]:
                path[next_node] = path[min_node].append(next_node)
                dis[next_node] = dis[min_node] + Graph[min_node][next_node]
        min_dis = INF
        for node in dis.keys():
            if node in booked_nodes:
                continue
            if dis[node] < min_dis:
                min_dis = dis[node]
                min_node = node
    return dis, path


G = {"V1": {"V2": 2, "V4": 1},
     "V2": {"V4": 3, "V5": 10},
     "V3": {"V1": 4, "V6": 5},
     "V4": {"V6": 8, "V7": 4, "V3": 2, "V5": 2},
     "V5": {"V7": 6},
     "V6": {},
     "V7": {"V6": 1}}

distance, path2node = Dijkstra(G, start="V1")
s = "V1"
print(distance)
print(path2node)
print("The start vertex is the V1\n")
for v in distance.keys():
    print("The shortest weighted path from %s to %s is : %d" % (s, v, distance[v]))
    print("The path is: %s \n" % ("->".join(path2node[v])))