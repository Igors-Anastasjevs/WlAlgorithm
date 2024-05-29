import openpyxl as xl
import WLalg
import time
import networkx as nx

def savedata(filename, Graphgenerator):
    data = dict()
    for size in range(30, 1510, 10):
        G = Graphgenerator(size)
        H = G.copy()
        data.update({size: []})
        for i in range(20):
            start = time.time()
            WLalg.wlalg(G, H)
            end = time.time()
            data[size].append(end - start)
        print('finished ', size)

    wb = xl.Workbook()
    ws = wb.active
    ws.title = 'data'
    i = 1
    for key in data.keys():
        ws.cell(row=i, column=1, value=key)
        for j in range(20):
            ws.cell(row=i, column=j + 2, value=data[key][j])
        i += 1
    wb.save(filename=filename)
savedata('data2.xlsx', nx.path_graph)