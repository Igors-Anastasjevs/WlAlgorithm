import WLalg
import networkx as nx
import WLalgShevarshidze
import savedata
graphs = savedata.generategraphs(nx.path_graph, range(30, 1510, 10))
savedata.savedata('outputs/data1.xlsx', graphs, WLalg.wlalg)
savedata.savedata('outputs/data2.xlsx', graphs, WLalgShevarshidze.wlalgV2)
savedata.savedata('outputs/data3.xlsx', graphs, nx.is_isomorphic)
graphs = savedata.generategraphs(nx.complete_graph, range(30, 610, 10))
savedata.savedata('outputs/data4.xlsx', graphs, WLalg.wlalg)
savedata.savedata('outputs/data5.xlsx', graphs, WLalgShevarshidze.wlalgV2)
savedata.savedata('outputs/data6.xlsx', graphs, nx.is_isomorphic)