
import time
import WLalg
import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math
g = nx.from_numpy_array(np.array([[0, 1, 1, 0],
                                          [1, 0, 0, 0],
                                          [1, 0, 0, 1],
                                          [0, 0, 1, 0]]), create_using=nx.DiGraph)
h = nx.from_numpy_array(np.array([[0, 0, 0, 1],
                                          [0, 0, 1, 1],
                                          [0, 1, 0, 0],
                                          [1, 1, 0, 0]]), create_using=nx.DiGraph)
#H = G.copy()
'''data = dict()
for size in range(30, 300):
    G = nx.path_graph(size)
    H = G.copy()
    data.update({size:[]})
    for i in range(20):
        start = time.time()
        WLalg.wlalg(G, H)
        end = time.time()
        data[size].append(end-start)'''
print(WLalg.wlalg(g, h))
'''
with open('data.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=';')
    for key in data.keys():
        w.writerow([key]+data[key])
'''

 #for drawing graph
'''
layout = nx.spring_layout(G)
nx.draw(H, layout, with_labels=True)
#labels = nx.get_edge_attributes(G, "weight")
#nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
plt.savefig("graphH.png")
plt.clf()
nx.draw(H, with_labels=True)
plt.savefig("graphG.png")'''

