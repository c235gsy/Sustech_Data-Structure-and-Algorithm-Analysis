# 3.Given an AOV network,
# generate and print a topological order if possible.


def topological_order(G):
    in_degrees = dict ((node, 0) for node in G.keys())
    for nodes in G.values():
        for node in nodes:
            in_degrees[node] += 1
    Q = [node for node in G.keys() if in_degrees[node] == 0]
    S = []
    while Q:
        node = Q.pop()
        S.append(node)
        for sub_node in G[node]:
            in_degrees[sub_node] -= 1
            if in_degrees[sub_node] == 0:
                Q.append(sub_node)
    return S


G = {'a': 'bf',
     'b': 'cdf',
     'c': 'd',
     'd': 'ef',
     'e': 'f',
     'f': ''}

print(str(topological_order(G))[1:-1])
