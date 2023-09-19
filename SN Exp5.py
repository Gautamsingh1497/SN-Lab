import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('E', 'F'),('F','G')])

unstable_triangles = 0
for node in G.nodes():
    neighbors = set(G.neighbors(node))
    for neighbor in neighbors:
        for second_neighbor in neighbors:
            if second_neighbor != neighbor and not G.has_edge(neighbor, second_neighbor):
                unstable_triangles += 1
print("Number of unstable triangles:", unstable_triangles)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500)
plt.show()

