import csv
from collections import defaultdict
from operator import length_hint
import sys

sys.setrecursionlimit(10**6)

ExGraph = {}
secondExGraph = {}

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    G = {}
    for node in tsv:
        make_link(G, node[0], node[1])
    return G

def read_graph_rev(filename):
    global ExGraph, secondExGraph
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter=" ")
    G = {}
    for node in tsv:
        if node[1] not in G:
            G[node[1]] = {}
            ExGraph[node[1]] = "unexplored"
            secondExGraph[node[1]] = "unexplored"
        (G[node[1]])[node[0]] = 1
        if node[0] not in G:
            G[node[0]] = {}
            ExGraph[node[0]] = "unexplored"
            secondExGraph[node[0]] = "unexplored"
    return G


def TopoSort(G):
    global total, CurLabel
    CurLabel = len(G)
    total = CurLabel
    for vertex in revG.keys():
        if ExGraph[vertex] == "unexplored":
            DFS_Topo(G, vertex)

countOne = 0
total = 0

def DFS_Topo(G, vertex):
    global CurLabel, total, countOne
    ExGraph[vertex] = "explored"
    open_list = [vertex]
    while (len(open_list) > 0):
        current = open_list[0]
        allPass = True
        for neighbour in G[current].keys():
            if ExGraph[neighbour] == "unexplored":
                allPass = False
                open_list.insert(0, neighbour)
                ExGraph[neighbour] = "explored"
                countOne += 1
                sys.stdout.flush()
                sys.stdout.write("\rstatus: {:6.2f}%".format(100.0 * countOne / total))          
        if allPass:
            del open_list[0]
            fs[CurLabel] = current
            CurLabel -= 1

def DFS_SCC(G, vertex):
    secondExGraph[vertex] = "explored"
    open_list = [vertex]
    while (len(open_list) > 0):
        current = open_list[0]
        del open_list[0]
        for neighbour in G[current].keys():
            if secondExGraph[neighbour] == "unexplored":
                scc[numSCC] += 1
                open_list.insert(0, neighbour)
                secondExGraph[neighbour] = "explored"

# Read the marvel comics graph
straightG = read_graph('graph.txt')
revG = read_graph_rev('graph.txt')

CurLabel = 0
fs = {}
TopoSort(revG)

numSCC = 0
scc = {}

length = len(fs)
count = 0
for order in sorted(fs.keys()):
    count += 1
    sys.stdout.flush()
    sys.stdout.write("\rstatus: {:6.2f}%".format(100.0 * count / length))
    if secondExGraph[fs[order]] == "unexplored":
        numSCC += 1
        scc[numSCC] = 1
        DFS_SCC(straightG, fs[order])
print()
print(numSCC)
print(sorted(scc.values()))