import networkx as nx
import matplotlib.pyplot as plt

def visualize_assignment(cost_matrix, row_ind, col_ind):
    G = nx.Graph()
    n = len(cost_matrix)

    for i in range(n):
        G.add_node(f"R{i}", bipartite=0)
        G.add_node(f"T{i}", bipartite=1)

    for i in range(n):
        for j in range(n):
            G.add_edge(f"R{i}", f"T{j}", weight=cost_matrix[i][j])

    pos = nx.bipartite_layout(G, nodes=[f"R{i}" for i in range(n)])
    edge_colors = ['red' if (f"R{i}", f"T{j}") in zip([f"R{x}" for x in row_ind], [f"T{y}" for y in col_ind]) else 'gray'
                  for i, j in G.edges()]

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color='lightblue', node_size=1000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Visualisation")
    plt.show()

# Example usage
cost = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = [0, 1, 2]
cols = [2, 1, 0]
visualize_assignment(cost, rows, cols)  