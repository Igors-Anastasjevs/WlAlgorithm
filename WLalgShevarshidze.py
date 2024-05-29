import networkx as nx
'''
def countneighbours(node, graph: nx.Graph):
    ''''''
    Counts neighbours
    :param node: input node
    :param graph: input graph
    :return: amount of neighbours, which a node has.
    :rtype:integer
    ''''''
    i = 0
    for n in graph.neighbors(node):
        i += 1
    return i
'''

def isEquivalent(labels: dict, graphG: nx.Graph, graphH: nx.Graph):
    '''
    Checks if 2 graphs have same labels
    :param dictionary labels: list of labels
    :param graphG: input graph
    :param graphH: input graph
    :return: True if they have, otherwise False
    '''
    labelG = []
    labelH = []
    for el in labels.keys():
        if el[0] == graphG:
            labelG.append(labels[el])
        elif el[0] == graphH:
            labelH.append(labels[el])
    labelG.sort()
    labelH.sort()
    if labelG == labelH:
        return True
    else:
        return False


class LabelCompressor():
    def __init__(self, graph: nx.Graph):
        '''
        Initialises itself, i.e. puts maximum amount of neighbours plus 1 as a feature, which is returned
        from this functor as element of its codomain
        :param graph: input graph
        '''
        self.featurelabel = 0
        for node in graph.nodes():
            cn = len(graph._adj[node])
            if cn > self.featurelabel:
                self.featurelabel = cn + 1
        self.features = dict()

    def __call__(self, string):
        '''
        Returns a compressed label, depending on input string. If string is not in self.features, self.featurelabel
        increments, string is saved in self.features and returns self.featurelabel
        :param string: input string
        :return: compressed label
        :rtype: integer
        '''
        if string in self.features:
            return self.features[string]
        else:
            self.featurelabel += 1
            self.features.update({string: self.featurelabel})
            return self.featurelabel
def init(graphG, graphH):
    '''
    Initialises dictionaries
    Labeling nodes is based on how many neighbours a node has
    :param graphG: input graph
    :param graphH: input graph
    :return: multiset-labels, labels
    '''
    multiset_labels = dict()
    labels = dict()
    for node in graphG.nodes:
        labels.update({(graphG, node): len(graphG._adj[node])})
    for node in graphH.nodes:
        labels.update({(graphH, node): len(graphH._adj[node])})
    for el in labels.keys():
        multiset_labels.update({el: [[labels[el]]]})
    return multiset_labels, labels
def stringcreation(multiset_labels, labels, i):
    '''
    Creates strings for each node
    :param multiset_labels: multiset of neighbours' labels for each node
    :param labels: labels for each node
    :param i: iteration
    :return: strings for each node
    '''
    strings = dict()
    for el in multiset_labels.keys():
        multiset_labels[el][i].sort()
        s = ''
        for l in multiset_labels[el][i]:
            s += str(l)
        s = str(labels[el]) + s
        if i == 0:
            strings.update({el: s})
        else:
            strings[el] = s
    return strings

def wlalgV2(graphG: nx.Graph, graphH: nx.Graph):
    '''
    Tells if 2 graphs are isomorphic implementing the Weisfeiler-Lehman algorithm, but it works differently
    :param graphG: input graph
    :param graphH: input graph
    :return: True if graphs are isomorphic, false otherwise
    '''
    if graphG.number_of_nodes() == graphH.number_of_nodes() and graphG.number_of_edges() == graphH.number_of_edges():

        labelcompressor = LabelCompressor(graphG)
        for i in range(graphG.number_of_nodes()):
            if i == 0:
                multiset_labels, labels = init(graphG, graphH)
            else:
                for el in multiset_labels.keys():
                    ls = []
                    for neighbours in el[0].neighbors(el[1]):
                        ls.append(labels[(el[0], neighbours)])
                    multiset_labels[el].append(ls)
            strings = stringcreation(multiset_labels, labels, i)
            for el in strings.keys():
                labels[el] = labelcompressor(strings[el])
            if not isEquivalent(labels, graphG, graphH):
                return False
        return True
    else:
        return False
