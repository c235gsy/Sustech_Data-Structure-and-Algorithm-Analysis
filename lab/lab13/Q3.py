# 3.Given an AOV network,
# generate and print a topological order if possible.


def topological_order(G):
    in_degrees = dict ((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            in_degrees[v] += 1
    Q = [u for u in G if in_degrees[u] == 0]
    S = []
    while Q:
        u = Q.pop ()
        S.append (u)
        for v in G[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                Q.append (v)
    return S


G = {'a': 'bf',
     'b': 'cdf',
     'c': 'd',
     'd': 'ef',
     'e': 'f',
     'f': ''}

print(str(topological_order(G))[1:-1])