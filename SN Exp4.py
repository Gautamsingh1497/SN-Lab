import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('E', 'F'),('F','G')])

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
influential_nodes_degree = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:5]
influential_nodes_betweenness = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:5]
influential_nodes_closeness = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:5]
nx.draw(G, with_labels=True)
print("Influential nodes based on degree centrality:", influential_nodes_degree)
print("Influential nodes based on betweenness centrality:", influential_nodes_betweenness)
print("Influential nodes based on closeness centrality:", influential_nodes_closeness)
plt.show()

