import mmh3
def similarity(M1, M2):
    if len(M1) == len(M2):
        Stsz1 = []
        Stsz2 = []
        for k in M1:
            Stsz1.append(len(M1[k]))
        for k in M2:
            Stsz2.append(len(M2[k]))
        if Stsz1 == Stsz2:
            return True
    return False

def wlalg(G, H):
    if (G.number_of_nodes()==H.number_of_nodes() or G.number_of_edges() == H.number_of_edges()):
        #print('G')
        CG = Canon(G)
        #print('H')
        CH = Canon(H)
        #print('G',CG,'\nH', CH)
        if similarity(CG, CH):
            return True
        else:
            return False
    else:
        return False
def Canon(G):
    M = []
    C = dict()
    for v in G.nodes:
        C.update({v:[1]})
    #print(C)
    i = 1
    M.append(dict({0:set()}))
    while i < len(G.nodes):
        for node in G.nodes:
            L = G.neighbors(node)
            col = ''
            for el in L:
                #print(G[node][el][0]['weight'])
                col += str(C[el][i-1])+str(G.get_edge_data(node, el, default=None))
            #print(46, node, col)
            C[node].append(mmh3.hash(col))
        #print(48, C)
        map = dict()
        for node in C:
            if C[node][i] in map:
                map[C[node][i]].add(node)
            else:
                map.update({C[node][i]: {node}})
        map = dict(sorted(map.items()))
        M.append(map)
        if similarity(M[i-1], M[i]):
            break
        i += 1

    return M[i-1]