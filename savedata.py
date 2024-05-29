import openpyxl as xl
import WLalg
import time
import networkx as nx

data = dict()
for size in range(30, 300):
    G = nx.path_graph(size)
    H = G.copy()
    data.update({size:[]})
    for i in range(20):
        start = time.time()
        WLalg.wlalg(G, H)
        end = time.time()
        data[size].append(end-start)

wb = xl.Workbook()
ws = wb.active
ws.title = 'data'

for key in data.keys():
    ws.cell(row=key-30+1, column=1, value=key)
    for i in range(20):
        ws.cell(row=key-30+1, column=i+1, value=data[key][i])
wb.save(filename='data1.xlsx')