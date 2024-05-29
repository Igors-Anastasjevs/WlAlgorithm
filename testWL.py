import unittest
import mmh3
import numpy as np
import WLalg
import networkx as nx

class WLTestCases(unittest.TestCase):

    def test_Similarity(self):
        '''
        This test case tests, how WLalg.similarity() detects similarity between dictionaries.
        '''
        M1 = {
            4:{1, 2, 3},
            5:{4, 5, 6}
        }
        M2 = {
            6: {1, 2, 3},
            7: {4, 5, 6}
        }
        self.assertTrue(WLalg.similarity(M1, M2))
        M1 = {
            4: {1, 2, 3},
            5: {4, 5, 6}
        }
        M2 = {
            6: {1, 2, 3},
            7: {4, 5, 6, 7}
        }
        self.assertFalse(WLalg.similarity(M1, M2))

    def test_Init(self):
        '''
        This test case tests how Wlalg.init() inititalizes array of maps m and map c.
        '''
        graph = nx.path_graph(3)
        m,c = WLalg.init(graph)
        self.assertIsInstance(m, list)
        self.assertIsInstance(c, dict)
        self.assertEqual(1, len(m))
        self.assertEqual(3, len(c))

    def test_GetColours(self):
        '''
        This small test case tests, how WLalg.getColours() collects labels/colours from 5-node graph G for node 1 at
        iteration 1.
        '''
        G = nx.path_graph(5)
        scolours = WLalg.getColours(G.neighbors(1), {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1, 1)
        self.assertEqual('111', scolours)

    def test_ColouringNodes(self):
        '''
        This small test case tests, how WLalg.colouringNodes() labels nodes in 5-node graph G at iteration 1.
        '''
        G = nx.path_graph(5)
        colours = WLalg.colouringNodes(G, {0: [1], 1: [1], 2: [1], 3: [1], 4: [1]}, 1)
        self.assertEqual({0: [1, mmh3.hash('11')], 1: [1, mmh3.hash('111')],
                          2: [1, mmh3.hash('111')], 3: [1, mmh3.hash('111')], 4: [1, mmh3.hash('11')]}, colours)

    def test_SortingNodes(self):
        '''
        This small test case tests, how WLalg.sortingNodes() sorts all nodes by their colours into 'map' dictionary
        at iteration 1.
        '''
        C = {0: [1, -1], 1: [1, -2], 2: [1, -2], 3: [1, -2], 4: [1, -1]}
        map = WLalg.sortingNodes(C, 1)
        self.assertEqual({-1: {0, 4}, -2: {1, 2, 3}},map)
    def test_GetCanonicalForm(self):
        '''
        This test case tests WLalg.getCanonicalForm() function
        '''
        G = nx.path_graph(5)
        CG = WLalg.getCanonicalForm(G)
        hash1 = mmh3.hash(str(mmh3.hash('11'))+str(mmh3.hash('111')))
        hash2 = mmh3.hash(str(mmh3.hash('111'))+str(mmh3.hash('11'))+str(mmh3.hash('111')))
        hash3 = mmh3.hash(str(mmh3.hash('111'))+str(mmh3.hash('111'))+str(mmh3.hash('111')))
        self.assertEqual({hash3: 1, hash2: 2, hash1: 2}, CG)

    def test_WLalg(self):
        '''
        This test case tests how WLalg.wlalg() states whether graphs are isomorphic or not.
        '''
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


if __name__ == '__main__':
    unittest.main()