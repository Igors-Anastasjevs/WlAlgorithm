import mmh3


def wlalg(G, H):
    if (G.number_of_nodes() == H.number_of_nodes() and G.number_of_edges() == H.number_of_edges()):
        if similarity(getCanonicalForm(G), getCanonicalForm(H)):
            return True
        else:
            return False
    else:
        return False


def getSizes(M):#map M -> array of int, which contains sizes of values by each key, assigning to index
    Stsz = []#array of sizes
    for k in M:
        Stsz.append(len(M[k]))
    return Stsz
def similarity(M1, M2):#map M1, map M2 -> True/False
    if len(M1) == len(M2):
        if getSizes(M1) == getSizes(M2):
            return True
    return False


def init(G):
    M = [dict({0:set()})]
    C = dict()
    for v in G.nodes:#
        C.update({v:[1]})
    return M, C
def getColours(graph, neighbours, colours, i, node):
    scolours = ''
    array = []
    for el in neighbours:
        array.append(str(colours[el][i - 1]) + str(graph.get_edge_data(node, el, default=None)))
    array.sort()
    for el in array:
        scolours += el
    return scolours

def colouringNodes(graph, colours, i):
    for node in graph.nodes:
        neighbours = graph.neighbors(node)
        colours[node].append(mmh3.hash(getColours(graph, neighbours, colours, i, node)))
    return colours
def sortingNodes(C, i):
    map = dict()
    for node in C:
        if C[node][i] in map:
            map[C[node][i]].add(node)
        else:
            map.update({C[node][i]: {node}})
    map = dict(sorted(map.items(), key=lambda x:x[1]))
    return map
def getCanonicalForm(G):#r
    M, C = init(G)
    i = 1
    while i < len(G.nodes):
        C = colouringNodes(G, C, i)
        map = sortingNodes(C, i)
        # print(map)
        M.append(map)
        if similarity(M[i-1], M[i]):
            break
        i += 1
    return M[i-1]