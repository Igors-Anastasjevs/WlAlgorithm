import networkx as nx

def countneighbours(node, graph:nx.Graph):
    '''
    Counts neighbours
    :param node: input node
    :param graph: input graph
    :return: amount of neighbours, which a node has.
    :rtype:integer
    '''
    i = 0
    for n in graph.neighbors(node):
        i += 1
    return i

class LabelCompressor():
    def __init__(self, graph:nx.Graph):
        '''
        Initialises itself, i.e. puts maximum amount of neighbours plus 1 as a feature, which is returned
        from this functor as element of its codomain
        :param graph: input graph
        '''
        self.featurelabel = 0
        for node in graph.nodes():
            cn = countneighbours(node,graph)
            if cn > self.featurelabel:
                self.featurelabel = cn + 1
        self.features = dict()
    def __call__(self, string):
        '''
        Returns a compressed label, depending on input string. If string is not in self.features, self.featurelabel increments
        and
        :param string: input string
        :return: compressed label
        :rtype: integer
        '''
        if string in self.features:
            return self.features[string]
        else:
            self.featurelabel += 1
            self.features.update({string:self.featurelabel})
            return self.featurelabel

def wlalgV2(graphG: nx.Graph, graphH: nx.Graph):
    '''
    Tells if 2 graphs are isomorphic implementing the Weisfeiler-Lehman algorithm, but it works differently
    :param graphG: input graph
    :param graphH: input graph
    :return: True if graphs are isomorphic, false otherwise
    '''
    if graphG.number_of_nodes() == graphH.number_of_nodes() and graphG.number_of_edges() == graphH.number_of_edges():
        multiset_labels = dict()
        labels = dict()
        strings = dict()
        labelcompressor = LabelCompressor(graphG)
        for i in range(graphG.number_of_nodes()):
            if i == 0:
                for node in graphG.nodes:
                    labels.update({(graphG,node):countneighbours(node, graphG)})
                for node in graphH.nodes:
                    labels.update({(graphH,node):countneighbours(node, graphH)})
                for el in labels.keys():
                    multiset_labels.update({el:[[labels[el]]]})
            else:
                for el in multiset_labels.keys():
                    ls = []
                    for neighbours in el[0].neighbors(el[1]):
                        ls.append(labels[(el[0],neighbours)])
                    multiset_labels[el].append(ls)
            for el in multiset_labels.keys():
                multiset_labels[el][i].sort()
                s = ''
                for l in multiset_labels[el][i]:
                    s += str(l)
                s = str(labels[el]) + s
                if i == 0:
                    strings.update({el:s})
                else:
                    strings[el] = s
            for el in strings.keys():
                labels[el] = labelcompressor(strings[el])
        return True
    else:
        return False