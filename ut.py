import unittest
import mmh3
import numpy as np
import WLalg
import networkx as nx
import WLaldShevarshidze as WLV2
class MyTestCase(unittest.TestCase):

    def testGetCanonicalForm(self):
        G = nx.path_graph(5)
        CG = WLalg.getCanonicalForm(G, lambda g,n,ne: '{}')
        hash1 = mmh3.hash(str(mmh3.hash('11{}'))+str(mmh3.hash('11{}1{}'))+'{}')
        hash2 = mmh3.hash(str(mmh3.hash('11{}1{}'))+str(mmh3.hash('11{}1{}'))+'{}'+str(mmh3.hash('11{}'))+'{}')
        hash3 = mmh3.hash(str(mmh3.hash('11{}1{}'))+str(mmh3.hash('11{}1{}'))+'{}'+str(mmh3.hash('11{}1{}'))+'{}')
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
        scolours = WLalg.getColours(G, G.neighbors(1), {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1, 1,lambda g,n,ne: '{}')
        self.assertEqual('11{}1{}', scolours)

    def testColouringNodes(self):
        G = nx.path_graph(5)
        colours = WLalg.colouringNodes(G, {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1, lambda g,n,ne: '{}')
        self.assertEqual({0: [1, mmh3.hash('11{}')], 1: [1, mmh3.hash('11{}1{}')],
                          2: [1, mmh3.hash('11{}1{}')], 3: [1, mmh3.hash('11{}1{}')], 4: [1, mmh3.hash('11{}')]}, colours)

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


if __name__ == '__main__':
    unittest.main()
