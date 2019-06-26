

def Dijkstra(G,s,INF=999):
    book = set()
    path = dict((k, []) for k in G.keys())
    minv = s
    dis = dict((k, INF) for k in G.keys())
    dis[s] = 0
    path[s] = [s]
    while len(book) < len(G):
        book.add(minv)
        for w in G[minv]:
            if dis[minv] + G[minv][w] < dis[w]:
                path[w] = path[minv] + [w]
                dis[w] = dis[minv] + G[minv][w]
        new = INF
        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis, path


G = {"V1": {"V2": 2, "V4": 1},
     "V2": {"V4": 3, "V5": 10},
     "V3": {"V1": 4, "V6": 5},
     "V4": {"V6": 8, "V7": 4, "V3": 2, "V5": 2},
     "V5": {"V7": 6},
     "V6": {},
     "V7": {"V6": 1}}

dis, path = Dijkstra(G, s="V1")
s = "V1"
print("The start vertex is the V1\n")
for v in dis.keys():
    print("The shortest weighted path from %s to %s is : %d" % (s, v, dis[v]))
    print("The path is: %s \n" % ("->".join(path[v])))