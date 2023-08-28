import networkx as nx
import matplotlib.pyplot as plt

G=nx.karate_club_graph()
communities=nx.community.greedy_modularity_communities(G)
membership={}
for i,comm in enumerate(communities):
    for node in comm:
        membership[node]=i
nx.set_node_attributes(G,membership,'community')
nx.write_gml(G,'karate.gml')
pos=nx.spring_layout(G)
node_colors = [membership[node] for node in G.nodes()]
plt.figure(figsize=(8, 5))
nx.draw_networkx(G, pos, node_color=node_colors, cmap="tab10", with_labels=True, node_size=300)
plt.title("Community Detection with Gephi")
plt.show()
