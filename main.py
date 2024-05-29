
import time
import WLalg
import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math
import openpyxl as xl
import WLalgShevarshidze

g = nx.complete_graph(5)
print(WLalg.getCanonicalForm(g))