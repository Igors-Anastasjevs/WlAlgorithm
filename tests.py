import unittest
import mmh3
import numpy as np
import WLalg
import networkx as nx
import WLalgShevarshidze as WLV2
class MyTestCase(unittest.TestCase):

    def testGetCanonicalForm(self):
        G = nx.path_graph(5)
        CG = WLalg.getCanonicalForm(G)
        hash1 = mmh3.hash(str(mmh3.hash('11'))+str(mmh3.hash('111')))
        hash2 = mmh3.hash(str(mmh3.hash('111'))+str(mmh3.hash('11'))+str(mmh3.hash('111')))
        hash3 = mmh3.hash(str(mmh3.hash('111'))+str(mmh3.hash('111'))+str(mmh3.hash('111')))
        self.assertEqual({hash3: 1, hash2: 2, hash1: 2}, CG)

    def testSimilarity(self):
        M1 = {
            4:{"1022", "2321", "1231"},
            5:{"1343", "1242", "2343"}
        }
        M2 = {
            6: {"1022", "2321", "1231"},
            7: {"1343", "1242", "2343"}
        }
        self.assertTrue(WLalg.similarity(M1, M2))
        M1 = {
            4: {"1022", "2321", "1231"},
            5: {"1343", "1242", "2343"}
        }
        M2 = {
            6: {"1022", "2321", "1231", "1002"},
            7: {"1343", "1242", "2343"}
        }
        self.assertFalse(WLalg.similarity(M1, M2))

    def testInit(self):
        graph = nx.path_graph(3)
        m,c = WLalg.init(graph)
        self.assertIsInstance(m, list)
        self.assertIsInstance(c, dict)
        self.assertEqual(1, len(m))
        self.assertEqual(3, len(c))

    def testWLalg(self):
        g = nx.path_graph(5)
        h = g.copy()
        self.assertTrue(WLalg.wlalg(g, h))
        g = nx.from_numpy_array(np.array([[0, 1, 1, 0],
                                          [1, 0, 0, 0],
                                          [1, 0, 0, 1],
                                          [0, 0, 1, 0]]), create_using=nx.DiGraph)
        h = nx.from_numpy_array(np.array([[0, 0, 0, 1],
                                          [0, 0, 1, 1],
                                          [0, 1, 0, 0],
                                          [1, 1, 0, 0]]), create_using=nx.DiGraph)
        self.assertTrue(WLalg.wlalg(g, h))
        g = nx.from_numpy_array(np.array([[0, 1, 1, 0],
                                          [1, 0, 0, 1],
                                          [1, 0, 0, 1],
                                          [0, 0, 1, 0]]), create_using=nx.DiGraph)
        h = nx.from_numpy_array(np.array([[0, 0, 0, 1],
                                          [0, 0, 1, 1],
                                          [0, 1, 0, 0],
                                          [1, 1, 0, 0]]), create_using=nx.DiGraph)
        self.assertFalse(WLalg.wlalg(g, h))

    def testGetColours(self):
        G = nx.path_graph(5)
        scolours = WLalg.getColours(G.neighbors(1), {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1, 1)
        self.assertEqual('111', scolours)

    def testColouringNodes(self):
        G = nx.path_graph(5)
        colours = WLalg.colouringNodes(G, {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1)
        self.assertEqual({0: [1, mmh3.hash('11')], 1: [1, mmh3.hash('111')],
                          2: [1, mmh3.hash('111')], 3: [1, mmh3.hash('111')], 4: [1, mmh3.hash('11')]}, colours)

    def testSortingNodes(self):
        C = {0: [1, -1], 1: [1, -2], 2: [1, -2], 3: [1, -2], 4: [1, -1]}
        map = WLalg.sortingNodes(C, 1)
        self.assertEqual({-1: {0, 4}, -2: {1, 2, 3}},map)

    def testShevashidze(self):

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
    def testInitandisEquivalentinWLV2(self):
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
    def testLabelCompressor(self):
        g = nx.path_graph(5)
        h = g.copy()
        lc = WLV2.LabelCompressor(g)
        self.assertEqual(2, lc.featurelabel)
        multiset_labels, labels = WLV2.init(g, h)
        strings = WLV2.stringcreation(multiset_labels, labels, 0)
        for el in strings.keys():
            labels[el] = lc(strings[el])
        correctanswer = {
            (g, 0): 3,
            (g, 1): 4,
            (g, 2): 4,
            (g, 3): 4,
            (g, 4): 3,
            (h, 0): 3,
            (h, 1): 4,
            (h, 2): 4,
            (h, 3): 4,
            (h, 4): 3
        }
        self.assertEqual(labels, correctanswer)
    def testStringcreation(self):
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

if __name__ == '__main__':
    unittest.main()
