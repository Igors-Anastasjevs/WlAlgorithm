import networkx as nx

def wlalgV2(graphG: nx.Graph, graphH: nx.Graph):
    '''
    Tells if 2 graphs are isomorphic implementing the Weisfeiler-Lehman algorithm from description from
    "Weisfeiler-Lehman Graph Kernel"
    by Shervashidze, N., Schweitzer, P., van Leeuwen, E. J., Mehlhorn, K., Borgwardt, K. M., Bach, F.[4].
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

def isEquivalent(labels: dict, graphG: nx.Graph, graphH: nx.Graph):
    '''
    Checks if 2 graphs have same labels.
    This function was not in Algorithm 1 from "Weisfeiler-Lehman Graph Kernel", but the paper says algorithm should finish
    "if the sets of newly created labels are not identical in G and G'" from page 2543 [4].
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

def init(graphG, graphH):
    '''
    Initialises dictionaries
    Labeling nodes is based on how many neighbours a node has.
    This function implements step 1 from Algorithm 1 from "Weisfeiler-Lehman Graph Kernel" [4]
    under condition that graph is not pre-labeled, and it is first iteration.
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

class LabelCompressor():
    '''
    This is function class, created in order to "compress" labels in order to implement step 3 in Algorithm 1 from [4]
    As it was written in my paper "Weisfeiler-Lehman Algorithm", "label compression" from [4] is different in comparison
    to this implementation, as there is no sorting.
    self.featurelabel is a member variable, integer, used to be assigned as a value to a string as a key.
    self.features is a dictionary, which has string as a key, which is a collection of nodes' and nodes' neighbours' labels
    and integer as a value, used as a new compressed label to the string.
    This functor implements step 3 from Algorithm 1 from "Weisfeiler-Lehman Graph Kernel"
    '''
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

def stringcreation(multiset_labels, labels, i):
    '''
    Creates strings for each node.
    This function implements step 2 from Algorithm 1 from "Weisfeiler-Lehman Graph Kernel" [4].
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

