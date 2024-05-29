import mmh3


def wlalg(G, H):
    '''
    Tells if 2 graphs are isomorphic
    :param networkx.Graph G: input graph
    :param networkx.Graph H: input graph
    :return: True/False
    '''
    if (G.number_of_nodes() == H.number_of_nodes() and G.number_of_edges() == H.number_of_edges()):
        if (getCanonicalForm(G).keys() == getCanonicalForm(H).keys()):
            return True
        else:
            return False
    else:
        return False



def similarity(M1, M2):
    '''
    Tells if 2 maps are similar
    :param dictionary M1: input dictionary
    :param dictionary M2: input dictionary
    :return: True/False
    '''
    if len(M1) == len(M2):
        for el in M1.values():
            if not(el in M2.values()):
                return False
        return True
    return False


def init(graph):
    '''
    Initialises array M and dictionary
    :param networkx.Graph graph: input graph
    :return: array of dictionary(-ies) M and dictionary C(colours)
    '''
    M = [dict({0:set()})]
    C = dict()
    for v in graph.nodes:
        C.update({v:[1]})
    return M, C

def getColours(graph, neighbours, colours, i, node):
    '''
    Returns string of neighbours' colours and adjacent edges' weights
    :param networkx.Graph graph: input graph
    :param list neighbours: neighbours of the node
    :param dictionary colours: data of colours in a previous iteration
    :param int i: iteration
    :param int node: library's way to access node
    :return: scolours
    :rtype: str
    '''
    scolours = ''
    array = []
    for el in neighbours:
        array.append(str(colours[el][i - 1]) + str(graph.get_edge_data(node, el, default=None)))
    array.sort()
    for el in array:
        scolours += el
    return scolours

def colouringNodes(graph, colours, i):
    '''
    Returns new colourings of nodes in the graph, preserving the old ones
    :param networkx.Graph graph:
    :param dictionary colours: data of colours in a previous iteration
    :param int i: iteration
    :return: dictionary colours
    '''
    for node in graph.nodes:
        neighbours = graph.neighbors(node)
        colours[node].append(mmh3.hash(getColours(graph, neighbours, colours, i, node)))
    return colours
def sortingNodes(colours, i):
    '''
    Sorts nodes by their colourings
    :param dictionary colours: new colours
    :param int i: iteration
    :return: dictionary of sorted nodes
    '''
    map = dict()
    for node in colours:
        if colours[node][i] in map:
            map[colours[node][i]].add(node)
        else:
            map.update({colours[node][i]: {node}})
    map = dict(sorted(map.items(), key=lambda x:x[1]))
    return map
def getCanonicalForm(graph):
    '''
    Returns canonical form of the input graph
    :param networkx.Graph graph: input graph
    :return: dictionary M[i-1]
    '''
    M, C = init(graph)
    i = 1
    while i < len(graph.nodes):
        C = colouringNodes(graph, C, i)
        map = sortingNodes(C, i)
        M.append(map)
        if similarity(M[i-1], M[i]):
            break
        i += 1
    M[i-1] = dict(sorted(M[i-1].items()))
    return M[i-1]