import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()
g.add_node(1)
g.add_nodes_from([2,3,4,5,6])
g.add_edges_from([(1,3),(2,4),(3,4),(4,5),(4,6),(6,5)])
nx.draw(g,with_labels=1)
plt.show()
