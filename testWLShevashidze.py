import unittest
import networkx as nx
import WLalgShevarshidze as WLV2
import numpy as np

class WLShevashidzeTestCases(unittest.TestCase):

    def test_Shevashidze(self):
        '''
        This test case tests, how WLV2.wlalgV2() states whether graphs are isomorphic or not.
        '''
        g = nx.path_graph(5)
        h = g.copy()
        self.assertTrue(WLV2.wlalgV2(g, h))
        g = nx.from_numpy_array(np.array([[0, 1, 1, 0],
                                          [1, 0, 0, 0],
                                          [1, 0, 0, 1],
                                          [0, 0, 1, 0]]), create_using=nx.DiGraph)
        h = nx.from_numpy_array(np.array([[0, 0, 0, 1],
                                          [0, 0, 1, 1],
                                          [0, 1, 0, 0],
                                          [1, 1, 0, 0]]), create_using=nx.DiGraph)
        self.assertTrue(WLV2.wlalgV2(g, h))

        g = nx.from_numpy_array(np.array([[0, 1, 1, 0],
                                          [1, 0, 0, 1],
                                          [1, 0, 0, 1],
                                          [0, 0, 1, 0]]), create_using=nx.DiGraph)
        h = nx.from_numpy_array(np.array([[0, 0, 0, 1],
                                          [0, 0, 1, 1],
                                          [0, 1, 0, 0],
                                          [1, 1, 0, 0]]), create_using=nx.DiGraph)
        self.assertFalse(WLV2.wlalgV2(g, h))

    def test_InitandisEquivalentinWLV2(self):
        '''
        This test case tests, how WLV2.init() initializes maps 'multi_label' and 'label', and WLV2.isEquivalent()
        states, whether 2 graphs have same set of labels.
        '''
        g = nx.path_graph(4)
        h = g.copy()
        multi_label, label = WLV2.init(g, h)
        ML = {(g, 0): [[1]],
              (g, 1): [[2]],
              (g, 2): [[2]],
              (g, 3): [[1]],
              (h, 0): [[1]],
              (h, 1): [[2]],
              (h, 2): [[2]],
              (h, 3): [[1]]
              }
        self.assertTrue(multi_label, ML)
        l = {
            (g, 0): 1,
            (g, 1): 2,
            (g, 2): 2,
            (g, 3): 1,
            (h, 0): 1,
            (h, 1): 2,
            (h, 2): 2,
            (h, 3): 1
        }
        self.assertTrue(l, label)
        self.assertTrue(WLV2.isEquivalent(l, g, h))

    def test_Stringcreation(self):
        '''
        This test case tests, how WLV2.stringcreation() collects each node's and its neighbours' labels.
        '''
        g = nx.path_graph(5)
        h = g.copy()
        lc = WLV2.LabelCompressor(g)
        self.assertEqual(2, lc.featurelabel)
        multiset_labels, labels = WLV2.init(g, h)
        strings = WLV2.stringcreation(multiset_labels, labels, 0)
        correctanswer = {
            (g, 0): '11',
            (g, 1): '22',
            (g, 2): '22',
            (g, 3): '22',
            (g, 4): '11',
            (h, 0): '11',
            (h, 1): '22',
            (h, 2): '22',
            (h, 3): '22',
            (h, 4): '11'
        }
        self.assertEqual(strings, correctanswer)

    def test_LabelCompressor(self):
        '''
        This test case tests, how methods of WLV2.LabelCompressor() work. i.e. if LabelCompressor.featurelabel is set
        in a right way for both identical 5-node graphs G and H, and if labels were compressed in a right way.
        '''
        G = nx.path_graph(5)
        H = G.copy()
        lc = WLV2.LabelCompressor(G)
        self.assertEqual(2, lc.featurelabel)
        multiset_labels, labels = WLV2.init(G, H)
        strings = WLV2.stringcreation(multiset_labels, labels, 0)
        for el in strings.keys():
            labels[el] = lc(strings[el])
        correctanswer = {
            (G, 0): 3,
            (G, 1): 4,
            (G, 2): 4,

            (G, 3): 4,
            (G, 4): 3,
            (H, 0): 3,
            (H, 1): 4,
            (H, 2): 4,
            (H, 3): 4,
            (H, 4): 3
        }
        self.assertEqual(labels, correctanswer)





if __name__ == '__main__':
    unittest.main()