import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('E', 'F'),('F','G')])

pagerank = nx.pagerank(G)
for node, value in pagerank.items():
    print("Node:", node, "PageRank:", value)