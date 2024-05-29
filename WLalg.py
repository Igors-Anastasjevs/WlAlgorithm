import mmh3
import networkx as nx


def wlalg(G:nx.Graph, H:nx.Graph, semfunc=lambda graph, node, neighbour: '{}'):
    '''
    Tells if 2 graphs are isomorphic implementing the Weisfeiler-Lehman algorithm
    :param function pointer semfunc: semantic function, expected to work with a graph, a node
    and one of the node's neighbour, be compatible with NetworkX library and return string value
    for proper colouring of node in a graph. Returns '{}' by default
    :param networkx.Graph G: input graph
    :param networkx.Graph H: input graph
    :return: True if graphs are isomorphic, false otherwise
    '''
    if G.number_of_nodes() == H.number_of_nodes() and G.number_of_edges() == H.number_of_edges():
        if getCanonicalForm(G, semfunc) == getCanonicalForm(H, semfunc):
            return True
        else:
            return False
    else:
        return False


def similarity(M1, M2):
    '''
    Tells if 2 maps are similar, ignoring the possible difference in keys.
    Similarity between 2 dictionaries is true if 2 dictionaries that have same sets
    e.g. these dicts:
    M1 = {-1915682609: {0, 4}, 985128023: {1, 3}, -776426510: {2}}
    M2 = {-959085024: {2}, 1018889979: {1, 3}, 1023573415: {0, 4}}
    are considered similar, since they have same sets {0, 4}, {1, 3} and {2}
    :param dictionary M1: input dictionary
    :param dictionary M2: input dictionary
    :return: True if both dicts contain exactly the same sets of values
    '''
    if len(M1) == len(M2):
        for el in M1.values():
            if not (el in M2.values()):
                return False
        return True
    return False


def init(graph:nx.Graph):
    '''
    Initialises array maps and dictionary.
    In detail it returns array with dictionary with 0 as key and empty set as value in order to properly compare
    2 dicts at first iteration
    :param networkx.Graph graph: input graph
    :return: array of dictionary(-ies) maps and dictionary colours
    '''
    maps = [dict({0: set()})]
    colours = dict()
    for v in graph.nodes:
        colours.update({v: [1]})
    return maps, colours


def getColours(graph, neighbours, colours, i, node, semfunc):
    '''
    Returns string of neighbours' colours and adjacent edges' weights
    It concatenates neighbours' colours and result of semantic function
    :param function pointer semfunc: semantic function, see 'def wlalg'
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
        array.append(str(colours[el][i - 1]) + semfunc(graph, node, el))
    array.sort()
    for el in array:
        scolours += el
    scolours = str(colours[node][i - 1])+scolours
    return scolours


def colouringNodes(graph, colours, i, semfunc):
    '''
    Returns new colourings of nodes in the graph, preserving the old ones
    :param function pointer semfunc: semantic function, see 'def wlalg'
    :param networkx.Graph graph: input graph
    :param dictionary colours: data of colours in a previous iteration
    :param int i: iteration
    :return: dictionary colours
    '''
    for node in graph.nodes:
        neighbours = graph.neighbors(node)
        colours[node].append(mmh3.hash(getColours(graph, neighbours, colours, i, node, semfunc)))
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
    map = dict(sorted(map.items(), key=lambda x: x[1]))
    return map


def getCanonicalForm(graph, semfunc):
    '''
    Returns canonical form of the input graph
    :param function pointer semfunc: semantic function, see 'def wlalg'
    :param networkx.Graph graph: input graph
    :return: dictionary M[i-1]
    '''
    maps, colours = init(graph)
    i = 1
    while i < len(graph.nodes):
        colours = colouringNodes(graph, colours, i, semfunc)
        map = sortingNodes(colours, i)
        maps.append(map)
        if similarity(maps[i - 1], maps[i]):
            break
        i += 1

    maps[i - 1] = dict(sorted(maps[i - 1].items()))
    Canonform = dict()
    for key in maps[i-1].keys():
        Canonform.update({key:len(maps[i-1][key])})
    return Canonform
