import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# G.add_node(8)
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6),(6,7)])
nx.draw(G,with_labels=1)
plt.show()
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_counts = nx.degree_histogram(G)
plt.bar(range(len(degree_counts)), degree_counts)
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title('Degree Distribution')
print(degree_sequence)
print(degree_counts)
plt.show()