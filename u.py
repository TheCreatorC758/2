import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_weighted_edges_from([(0, 1, 1), (0, 2, 3), (1, 3, 5), (2, 3, 1), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 4)])

start_node, goal_node = 0, 5

try:
    shortest_path = nx.shortest_path(G, source=start_node, target=goal_node, weight='weight')
    shortest_path_length = nx.shortest_path_length(G, source=start_node, target=goal_node, weight='weight')

    edge_colors = ['red' if (u, v) in zip(shortest_path, shortest_path[1:]) else 'gray' for u, v in G.edges()]

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color=edge_colors, arrows=True)
    nx.draw_networkx_edges(G, pos,  width=2.0, alpha=0.5, edge_color='blue')

    print(f"Minimum cost from {start_node} to {goal_node} is = {shortest_path_length}")
except nx.NetworkXNoPath:
    print(f"No path exists from {start_node} to {goal_node}.")
plt.show()