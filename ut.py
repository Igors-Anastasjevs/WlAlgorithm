import unittest

import mmh3

import WLalg
import networkx as nx
class MyTestCase(unittest.TestCase):
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
        #assfalse
    def testGetSizes(self):
        M = {
            4:{"1", "2", "3"}
        }
        self.assertEqual(WLalg.getSizes(M), [3])
    def testInit(self):
        graph = nx.path_graph(3)
        m,c = WLalg.init(graph)
        self.assertIsInstance(m, list)
        self.assertIsInstance(c, dict)
        self.assertEqual(1, len(m))
        self.assertEqual(3, len(c))
    def testGetCanonicalForm(self):
        G = nx.path_graph(5)
        CG = WLalg.getCanonicalForm(G)
        #self.assertEqual({-1915682609: {0}, -1013786334: {2}, -706418556: {1}, 985128023: {3}, 1971917593: {4}}, CG)
    def testGetColours(self):
        G = nx.path_graph(5)
        scolours = WLalg.getColours(G, G.neighbors(1), {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1, 1)
        self.assertEqual('1{}1{}', scolours)
    def testColouringNodes(self):
        G = nx.path_graph(5)
        colours = WLalg.colouringNodes(G, {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1)
        self.assertEqual({0: [1, mmh3.hash('1{}')], 1: [1, mmh3.hash('1{}1{}')], 2: [1, mmh3.hash('1{}1{}')], 3: [1, mmh3.hash('1{}1{}')], 4: [1, mmh3.hash('1{}')]}, colours)
    def testSortingNodes(self):
        C = {0: [1, -1], 1: [1, -2], 2: [1, -2], 3: [1, -2], 4: [1, -1]}
        map = WLalg.sortingNodes(C, 1)
        self.assertEqual({-1: {0, 4}, -2: {1, 2, 3}},map)
if __name__ == '__main__':
    unittest.main()
